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

        # --- Stack Positioning ---
        undo_stack = VGroup().arrange(DOWN, buff=0.1).next_to(undo_title, DOWN, buff=0.4)
        redo_stack = VGroup().arrange(DOWN, buff=0.1).next_to(redo_title, DOWN, buff=0.4)

        # Helper to create a stack box
        def create_box(text, color):
            box = Rectangle(height=0.6, width=2.5, color=box_color)
            label = Text(text, color=color).scale(0.5)
            label.move_to(box.get_center())
            return VGroup(box, label)

        # Animate pushing to a stack
        def push_to_stack(stack_group, text, color, direction=DOWN):
            box = create_box(text, color)
            if stack_group:
                box.next_to(stack_group[0], direction, buff=0.1)
                stack_group.add(box)
            else:
                box.next_to(undo_title if direction == DOWN else redo_title, DOWN, buff=0.4)
                stack_group.add(box)
            self.play(FadeIn(box, shift=UP), run_time=0.4)
            return box

        # Animate popping from a stack
        def pop_from_stack(stack_group):
            if stack_group:
                box = stack_group[0]
                stack_group.remove(box)
                self.play(FadeOut(box, shift=UP), run_time=0.4)
                return box
            return None

        # Sync the stacks
        def update_stacks():
            for i, box in enumerate(undo_stack):
                box.move_to(undo_title.get_bottom() - DOWN * (i + 1) * 0.7)
            for i, box in enumerate(redo_stack):
                box.move_to(redo_title.get_bottom() - DOWN * (i + 1) * 0.7)
            self.play(LaggedStart(*[
                box.animate.move_to(box.get_center()) for box in undo_stack + redo_stack
            ], lag_ratio=0.1), run_time=0.4)

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
                push_to_stack(undo_stack, text, text_color)
                for redo_box in redo_stack:
                    self.play(FadeOut(redo_box, shift=DOWN), run_time=0.2)
                redo_stack.clear()
            elif op == "undo":
                action = manager.undo()
                if action:
                    box = pop_from_stack(undo_stack)
                    if box:
                        push_to_stack(redo_stack, action, text_color)
            elif op == "redo":
                action = manager.redo()
                if action:
                    box = pop_from_stack(redo_stack)
                    if box:
                        push_to_stack(undo_stack, action, text_color)
            update_stacks()
            self.wait(0.3)

        # Final Pause
        self.wait(2)
