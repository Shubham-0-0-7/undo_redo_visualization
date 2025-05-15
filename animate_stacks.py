from manim import *
import undo_redo as ur

class UndoRedoAnimation(Scene):
    def construct(self):
        undo_title = Text("Undo Stack", color=BLUE).scale(0.6).to_corner(UL)
        redo_title = Text("Redo Stack", color=RED).scale(0.6).to_corner(UR)
        curr_title = Text("Current String:", color=YELLOW).scale(0.6).to_edge(DOWN).shift(UP * 0.2)
        curr_text = Text("", color=WHITE).scale(0.6).next_to(curr_title, DOWN)
        operation_text = Text("", color=GREEN_E).scale(0.8).move_to(ORIGIN)

        self.play(Write(undo_title), Write(redo_title), Write(curr_title), Write(curr_text))
        self.wait(0.5)

        undo_stack = VGroup()
        redo_stack = VGroup()

        def create_box(content, color=WHITE):
            rect = Rectangle(height=0.6, width=3, color=color)
            label = Text(content, color=color).scale(0.45)
            label.move_to(rect.get_center())
            return VGroup(rect, label)

        def update_curr_text():
            new_text = Text(ur.curr, color=WHITE).scale(0.6).next_to(curr_title, DOWN)
            self.play(Transform(curr_text, new_text), run_time=0.6)

        def show_operation(message):
            op = Text(message, color=GREEN_E).scale(0.8).move_to(ORIGIN)
            self.play(Transform(operation_text, op), run_time=0.6)
            self.wait(0.4)

        def push_stack(stack_group, content, is_undo=True):
            box = create_box(content)
            if len(stack_group) > 0:
                box.next_to(stack_group[-1], DOWN, buff=0.1)
            else:
                ref = undo_title if is_undo else redo_title
                box.next_to(ref, DOWN, buff=0.3)
            stack_group.add(box)
            self.play(FadeIn(box, shift=UP), run_time=0.6)

        def pop_stack(stack_group):
            if len(stack_group) > 0:
                box = stack_group[-1]
                stack_group.remove(box)
                self.play(FadeOut(box, shift=UP), run_time=0.6)

        def clear_stack(stack_group):
            while len(stack_group) > 0:
                pop_stack(stack_group)

        ur.curr = ""
        ur.undotop = -1
        ur.redotop = -1
        ur.pushundo(ur.curr)
        push_stack(undo_stack, ur.curr, is_undo=True)
        update_curr_text()

        actions = [
            ("append", "Hi"),
            ("append", " "),
            ("append", "Shubham"),
            ("undo", None),
            ("undo", None),
            ("redo", None),
            ("append", "!!"),
            ("undo", None),
            ("redo", None),
            ("redo", None),  
        ]

        for action, text in actions:
            if action == "append":
                ur.curr = (ur.curr + text)[:ur.MAXSIZE - 1]
                show_operation(f"Append '{text}'")
                ur.pushundo(ur.curr)
                push_stack(undo_stack, ur.curr, is_undo=True)
                ur.clearredo()
                clear_stack(redo_stack)
            elif action == "undo":
                if ur.undotop > 0:
                    show_operation("Undo")
                    ur.pushredo(ur.curr)
                    push_stack(redo_stack, ur.curr, is_undo=False)
                    ur.undotop -= 1
                    pop_stack(undo_stack)
                    ur.curr = ur.undo[ur.undotop]
                else:
                    show_operation("Undo (nothing to undo)")
            elif action == "redo":
                if ur.redotop >= 0:
                    show_operation("Redo")
                    ur.pushundo(ur.curr)
                    push_stack(undo_stack, ur.curr, is_undo=True)
                    ur.curr = ur.redo[ur.redotop]
                    ur.redotop -= 1
                    pop_stack(redo_stack)
                else:
                    show_operation("Redo (nothing to redo)")
            update_curr_text()
            self.wait(0.7)

        self.wait(2)
