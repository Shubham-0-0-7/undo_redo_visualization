from manim import *
from undo_redo import UndoRedoManager

class UndoRedoStackScene(Scene):
    def construct(self):
        # Setup
        manager = UndoRedoManager()

        # --- Colors ---
        undo_color = BLUE_E
        redo_color = RED_E
        box_color = WHITE
        text_color = YELLOW_E

        # --- Titles ---
        undo_title = Text("Undo Stack", color=undo_color).scale(0.6).to_corner(UL)
        redo_title = Text("Redo Stack", color=redo_color).scale(0.6).to_corner(UR)
        self.play(Write(undo_title), Write(redo_title))

        # --- Stack Groups ---
        undo_stack_group = VGroup()
        redo_stack_group = VGroup()
        undo_stack_group.next_to(undo_title, DOWN, buff=0.4)
        redo_stack_group.next_to(redo_title, DOWN, buff=0.4)

        # Helper to create a stack box
        def create_box(text, color):
            box = Rectangle(height=0.6, width=2.5, color=box_color)
            label = Text(text, color=color).scale(0.5)
            label.move_to(box.get_center())
            return VGroup(box, label)

        # Animate pushing to a stack
        def push_to_stack(stack_group, text, color):
            box = create_box(text, color)
            if len(stack_group) > 0:
                box.next_to(stack_group[-1], DOWN, buff=0.1)
            else:
                if stack_group == undo_stack_group:
                    box.next_to(undo_title, DOWN, buff=0.4)
                else:
                    box.next_to(redo_title, DOWN, buff=0.4)
            
            stack_group.add(box)
            self.play(FadeIn(box, shift=UP), run_time=0.4)
            return box

        # Animate popping from a stack
        def pop_from_stack(stack_group):
            if len(stack_group) > 0:
                box = stack_group[-1]
                stack_group.remove(box)
                self.play(FadeOut(box, shift=UP), run_time=0.4)
                return box
            return None

        # Example Operations:
        ops = [
            ("append", "Draw circle"),
            ("append", "Draw square"),
            ("append", "Erase circle"),
            ("undo", None),
            ("undo", None),
            ("redo", None),
            ("append", "Draw triangle"),
            ("undo", None),
        ]

        for op, text in ops:
            if op == "append":
                manager.append(text)
                push_to_stack(undo_stack_group, text, text_color)
                # Clear redo stack visually
                for box in reversed(redo_stack_group):
                    self.play(FadeOut(box, shift=DOWN), run_time=0.2)
                redo_stack_group = VGroup()
            elif op == "undo":
                action = manager.undo()
                if action:
                    box = pop_from_stack(undo_stack_group)
                    if box:
                        push_to_stack(redo_stack_group, action, text_color)
            elif op == "redo":
                action = manager.redo()
                if action:
                    box = pop_from_stack(redo_stack_group)
                    if box:
                        push_to_stack(undo_stack_group, action, text_color)
            self.wait(0.3)

        # Final Pause
        self.wait(2)