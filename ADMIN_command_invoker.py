#ADMIN_command_invoker.py
# Purpose: Invokes and manages command execution and history for undo functionality.
# Design Pattern: Command Pattern - Handles command execution and supports undo.
# Principle: SRP - Only responsible for executing and undoing commands.
# Linked Files: Works with Command objects (Add, Edit, Delete) to manage history.


class CommandInvoker:
    def __init__(self):
        self.history = [] # Stores executed commands for undo

    def execute_command(self, command):
        # Executes a command and saves it to history if undo is supported
        command.execute() 
   
        if hasattr(command, "undo") and callable(getattr(command, "undo", None)):
            self.history.append(command)

    def undo_last(self):
        # Undoes the last executed command if available
        if self.history:
            command = self.history.pop()
            command.undo()

