class UndoRedoManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def append(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            return action
        return None

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            return action
        return None

    def get_undo_stack(self):
        return self.undo_stack.copy()

    def get_redo_stack(self):
        return self.redo_stack.copy()