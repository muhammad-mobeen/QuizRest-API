import json
import random

class MCQsParser:
    def __init__(self, filepath, number):
        self.filepath = filepath
        self.number = number
        self.bank = {"mcqs":[]}
    

    def get_response(self, type="dict"):
        self.read_file()
        if self.number < 20:
            self.bank["mcqs"] = self.bank["mcqs"][:self.number]
            self.bank["total_questions"] = len(self.bank["mcqs"])

            if type == "json":
                return json.dumps(self.bank, indent=2, sort_keys=False)
            else:
                return self.bank
        else:
            self.bank["total_questions"] = len(self.bank["mcqs"])
            
            if type == "json":
                return json.dumps(self.bank, indent=2, sort_keys=False)
            else:
                return self.bank      
    
    
    def read_file(self):
        with open(self.filepath) as f:
            lines = f.readlines()
        self.parse_file(lines)


    def parse_file(self, line_list):
        mcq = {}
        flag = {  # Records states of parse enumeration
            "read": "question",
            "id": 0,
            "choice": 0
            }
        for i,item in enumerate(line_list,1):
            if flag["read"] == "question":
                mcq["id"] = flag["id"]
                mcq["question"] = item.strip('\n')
                mcq["choices"] = []
                # Set Flags for next itteration
                flag["read"] = "choice"
            elif flag["read"] == "choice":
                if flag["choice"] == 0:
                    mcq["correct_answer"] = item.strip('\n')
                if flag["choice"] < 4:
                    mcq["choices"].append(item.strip('\n'))
                    # Set Flags for next itteration
                    flag["choice"] += 1
                else:
                    random.shuffle(mcq["choices"])  # randomize the order of choices
                    self.bank["mcqs"].append(mcq)
                    mcq = {}
                    flag["read"] = "question"
                    flag["id"] += 1
                    flag["choice"] = 0

        # Shuffling starts here
        random.shuffle(self.bank["mcqs"])
        for i,mcq in enumerate(self.bank["mcqs"]):
            new = {"index": i}
            new.update(mcq)
            self.bank["mcqs"][i] = new


if __name__ == "__main__":
    filepath = "mcqs_bank.txt"
    number = 5
    agent = MCQsParser(filepath, number)
    print(agent.get_response("json"))