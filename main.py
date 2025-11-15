#!/usr/bin/env python3
"""
AI Agent using LangChain and Google Gemini
A simple but powerful AI agent that can engage in conversations and perform tasks.

Created by Sachin
LinkedIn: https://www.linkedin.com/in/sachin-pradhan-ba82a927a
"""

import os
import sys
from typing import Optional, List, Dict, Any
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
# from langchain_community.callbacks import get_openai_callback  # Not needed for Gemini
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt
from rich import print as rprint


class AIAgent:
    """A sophisticated AI Agent using Google Gemini via LangChain."""
    
    def __init__(self, model_name: str = "models/gemini-2.0-flash", temperature: float = 0.7):
        """Initialize the AI Agent with Gemini model."""
        # Load environment variables
        load_dotenv()
        
        # Validate API key
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        
        # Initialize console for rich output
        self.console = Console()
        
        # Initialize the Gemini model
        try:
            self.llm = ChatGoogleGenerativeAI(
                model=model_name,
                temperature=temperature,
                google_api_key=self.api_key
            )
        except Exception as e:
            self.console.print(f"[red]Error initializing Gemini model: {e}[/red]")
            raise
        
        # Agent personality and capabilities
        self.system_prompt = """You are a helpful and intelligent AI agent built with LangChain and Google Gemini. 
        You are capable of:
        - Having natural conversations
        - Answering questions across various domains
        - Helping with problem-solving
        - Providing explanations and tutorials
        - Assisting with creative tasks
        - Code assistance and debugging
        
        Be friendly, helpful, and engaging. Provide detailed and accurate responses.
        If you're unsure about something, be honest about it.
        """
        
        # Initialize conversation history
        self.conversation_history: List[Dict[str, Any]] = []
        
        # Create the conversation chain
        self.setup_chain()
    
    def setup_chain(self) -> None:
        """Set up the conversation chain with prompt template."""
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}")
        ])
        
        # Create the chain
        self.chain = (
            RunnablePassthrough.assign(
                chat_history=lambda x: self.conversation_history
            )
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
    
    def add_to_history(self, human_message: str, ai_message: str) -> None:
        """Add messages to conversation history."""
        self.conversation_history.extend([
            HumanMessage(content=human_message),
            AIMessage(content=ai_message)
        ])
        
        # Keep history manageable (last 20 exchanges)
        if len(self.conversation_history) > 40:
            self.conversation_history = self.conversation_history[-40:]
    
    def get_response(self, user_input: str) -> str:
        """Get response from the AI agent."""
        try:
            response = self.chain.invoke({"input": user_input})
            self.add_to_history(user_input, response)
            return response
        except Exception as e:
            error_msg = f"Error getting response: {e}"
            self.console.print(f"[red]{error_msg}[/red]")
            # Print the full error for debugging
            import traceback
            print(f"Full error traceback: {traceback.format_exc()}")
            return f"I'm sorry, I encountered an error while processing your request. Error: {str(e)}"
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        self.conversation_history.clear()
        self.console.print("[yellow]Conversation history cleared![/yellow]")
    
    def show_history(self) -> None:
        """Display conversation history."""
        if not self.conversation_history:
            self.console.print("[yellow]No conversation history yet.[/yellow]")
            return
        
        self.console.print("\n[bold blue]Conversation History:[/bold blue]")
        for i, message in enumerate(self.conversation_history):
            role = "Human" if isinstance(message, HumanMessage) else "AI"
            color = "green" if role == "Human" else "blue"
            self.console.print(f"[{color}]{role}:[/{color}] {message.content}")
            if i < len(self.conversation_history) - 1:
                self.console.print()
    
    def interactive_mode(self) -> None:
        """Start interactive conversation mode."""
        self.console.print(Panel.fit(
            "[bold green]Welcome to the AI Agent![/bold green]\n"
            "Powered by LangChain and Google Gemini\n\n"
            "Commands:\n"
            "- Type your message to chat\n"
            "- '/help' for help\n"
            "- '/clear' to clear history\n"
            "- '/history' to show conversation history\n"
            "- '/quit' or '/exit' to quit\n\n"
            "[dim]Created by Sachin | LinkedIn: https://www.linkedin.com/in/sachin-pradhan-ba82a927a[/dim]",
            title="AI Agent",
            border_style="green"
        ))
        
        while True:
            try:
                user_input = Prompt.ask("\n[bold green]You[/bold green]")
                
                if user_input.lower() in ['/quit', '/exit', 'quit', 'exit']:
                    self.console.print("[yellow]Goodbye! Thanks for chatting![/yellow]")
                    break
                elif user_input.lower() == '/clear':
                    self.clear_history()
                    continue
                elif user_input.lower() == '/history':
                    self.show_history()
                    continue
                elif user_input.lower() == '/help':
                    self.show_help()
                    continue
                elif not user_input.strip():
                    continue
                
                # Get AI response
                self.console.print("[yellow]Thinking...[/yellow]", end="")
                response = self.get_response(user_input)
                self.console.print("\r" + " " * 20 + "\r", end="")  # Clear "Thinking..."
                
                # Display response with markdown support
                self.console.print("\n[bold blue]AI Agent:[/bold blue]")
                self.console.print(Panel(Markdown(response), border_style="blue"))
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Goodbye! Thanks for chatting![/yellow]")
                break
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")
    
    def show_help(self) -> None:
        """Show help information."""
        help_text = """
        [bold blue]AI Agent Help[/bold blue]
        
        [green]Available Commands:[/green]
        - [yellow]/help[/yellow] - Show this help message
        - [yellow]/clear[/yellow] - Clear conversation history
        - [yellow]/history[/yellow] - Show conversation history
        - [yellow]/quit[/yellow] or [yellow]/exit[/yellow] - Exit the program
        
        [green]Features:[/green]
        - Natural conversation with context memory
        - Code assistance and debugging
        - Creative writing and brainstorming
        - Question answering across various domains
        - Problem-solving assistance
        
        Just type your message and press Enter to chat!
        """
        self.console.print(Panel(help_text, title="Help", border_style="cyan"))


def main():
    """Main function to run the AI Agent."""
    try:
        # Initialize the agent
        agent = AIAgent()
        
        # Check if running in interactive mode
        if len(sys.argv) > 1:
            # Command line mode
            query = " ".join(sys.argv[1:])
            console = Console()
            console.print(f"[green]Query:[/green] {query}")
            response = agent.get_response(query)
            console.print(f"\n[blue]Response:[/blue]\n{response}")
        else:
            # Interactive mode
            agent.interactive_mode()
            
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        console = Console()
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()