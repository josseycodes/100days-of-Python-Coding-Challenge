from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter


class CodeSnippet:
    def __init__(self, name, language, code, category=None):
        self.name = name
        self.language = language
        self.code = code
        self.category = category

    def display(self):
        lexer = get_lexer_by_name(self.language)
        formatter = TerminalFormatter()
        formatted_code = highlight(self.code, lexer, formatter)
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(formatted_code)


class CodeSnippetManager:
    def __init__(self):
        self.snippets = []

    def add_snippet(self, snippet):
        self.snippets.append(snippet)

    def search_snippets(self, keyword):
        found_snippets = []
        for snippet in self.snippets:
            if keyword.lower() in snippet.name.lower() or (snippet.category and keyword.lower() in snippet.category.lower()):
                found_snippets.append(snippet)
        return found_snippets

    def display_snippets(self, snippets):
        if snippets:
            for snippet in snippets:
                snippet.display()
                print()
        else:
            print("No snippets found.")

    def display_all_snippets(self):
        if self.snippets:
            for snippet in self.snippets:
                snippet.display()
                print()
        else:
            print("No snippets available.")


def main():
    snippet_manager = CodeSnippetManager()

    while True:
        print("\nCode Snippet Manager Menu:")
        print("1. Add Snippet")
        print("2. Search Snippets")
        print("3. Display All Snippets")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter snippet name: ")
            language = input("Enter programming language: ")
            code = input("Enter code: ")
            category = input("Enter category (optional): ")
            snippet = CodeSnippet(name, language, code, category)
            snippet_manager.add_snippet(snippet)
            print("Snippet added successfully.")
        elif choice == '2':
            keyword = input("Enter keyword to search: ")
            found_snippets = snippet_manager.search_snippets(keyword)
            snippet_manager.display_snippets(found_snippets)
        elif choice == '3':
            snippet_manager.display_all_snippets()
        elif choice == '4':
            print("Exiting Code Snippet Manager.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
