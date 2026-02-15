print("---" * 10)

class cyberTool:
    def __init__(self, tool_name, topic_kind):
        self.name = tool_name
        self.topic = topic_kind
        self.log = []
        print(f"--- {self.name} Module is ready! ---")

    def scan(self, target):
        print(f"Scanning {target} for {self.topic} vulnerabilities...")
        self.log.append(f"Scanned {target} for {self.topic} vulnerabilities.")

    def report(self):
        print(f"Report: with {self.name}, these have been scanned until now: {self.log}")

scanner = cyberTool("VulnScanner", "web")
scanner.scan("example.com")
scanner.report()
print(f"Topic/Kind of this tool: {scanner.topic}")

print("---" * 10)

class Developer:
    def __init__(self, name, language, mode):
        self.name = name
        self.language = language
        self.mode = mode
        print(f"--- Developer {self.name} is ready! ---")

    def code(self):
        print(f"{self.name} is coding in {self.language}.")

    def mood(self):
        print(f"{self.name} is currently in {self.mode} mode.")

dev1 = Developer("MFK", "Python", "Happy")
dev1.code()
dev1.mood()

print("---" * 10)
