import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { ScrollArea } from "@/components/ui/scroll-area";
import {
	Card,
	CardContent,
	CardFooter,
	CardHeader,
	CardTitle,
} from "@/components/ui/card";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";

import axios from "axios";
import MarkdownRenderer from "./ui/markdown-renderer";

interface Message {
	id: number;
	text: string;
	sender: string;
}

const Chat = () => {
	const [messages, setMessages] = useState<Message[]>([
		{ id: 1, text: "Hello! How can I assist you today?", sender: "bot" },
	]);
	const [inputMessage, setInputMessage] = useState("");

	const handleSendMessage = async () => {
		if (inputMessage.trim() !== "") {
			setMessages([
				...messages,
				{ id: messages.length + 1, text: inputMessage, sender: "user" },
			]);
			setInputMessage("");
			// Simulate bot response
			try {
				// Replace URL with your server's endpoint
				const response = await axios.post(
					"http://localhost:8000/query",
					{ query: inputMessage }
				);
				console.log(response.data);
				const serverMessage = response?.data?.response?.answer; // Assuming the response contains a message

				// Add server response to chat
				setMessages((prevMessages) => [
					...prevMessages,
					{
						id: messages.length + 1,
						sender: "server",
						text: serverMessage,
					},
				]);
			} catch (error) {
				console.error("Error sending message:", error);
				setMessages((prevMessages) => [...prevMessages.slice(0, -1)]); // Remove user message from chat if sending failed
			}
		}
	};

	return (
		<Card className="w-full max-w-md mx-auto">
			<CardHeader>
				<CardTitle>Prof Finder</CardTitle>
			</CardHeader>
			<CardContent>
				<ScrollArea className="h-[400px] pr-4">
					{messages.map((message) => (
						<div
							key={message.id}
							className={`flex ${
								message.sender === "user"
									? "justify-end"
									: "justify-start"
							} mb-4`}
						>
							<div
								className={`flex items-start ${
									message.sender === "user"
										? "flex-row-reverse"
										: "flex-row"
								}`}
							>
								<Avatar className="w-8 h-8">
									<AvatarFallback>
										{message.sender === "user" ? "U" : "B"}
									</AvatarFallback>
								</Avatar>
								<div
									className={`mx-2 p-3 rounded-lg ${
										message.sender === "user"
											? "bg-primary text-primary-foreground"
											: "bg-muted"
									}`}
								>
									<MarkdownRenderer content={typeof message.text === "string" ? message.text : JSON.stringify(message.text)} />
								</div>
							</div>
						</div>
					))}
				</ScrollArea>
			</CardContent>
			<CardFooter>
				<form
					onSubmit={(e) => {
						e.preventDefault();
						handleSendMessage();
					}}
					className="flex w-full space-x-2"
				>
					<Input
						placeholder="Type your message..."
						value={inputMessage}
						onChange={(e) => setInputMessage(e.target.value)}
					/>
					<Button type="submit">Send</Button>
				</form>
			</CardFooter>
		</Card>
	);
}

export default Chat;