import json

class MCQsParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.bank = dict()

    def read_file(self):
        with open(self.filepath) as f:
            lines = f.readlines()
        self.parse_file(lines)

    def parse_file(self, line_list):
        mcq = {}
        flag = {  # Records states of parse enumeration
            "read": "question",
            "index": 0,
            "choice": 0
            }
        for i,item in enumerate(line_list,1):
            if flag["read"] == "question":
                mcq["index"] = flag["index"]
                mcq["question"] = item.strip('\n')
                mcq["choices"] = []
                # Set Flags for next itteration
                flag["read"] = "choice"
            elif flag["read"] == "choice":
                if flag["choice"] < 4:
                    mcq["choices"].append(item.strip('\n'))
                    # Set Flags for next itteration
                    flag["choice"] += 1
                else:
                    self.bank["question{}".format(flag["index"])] = mcq
                    mcq = {}
                    flag["read"] = "question"
                    flag["index"] += 1
                    flag["choice"] = 0
        print(json.dumps(self.bank, indent=2, sort_keys=True))
        print(len(self.bank))






if __name__ == "__main__":
    filepath = "mcqs_bank.txt"
    agent = MCQsParser(filepath)
    agent.read_file()