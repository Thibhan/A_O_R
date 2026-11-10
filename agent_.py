# agent
# agent extract the in formation ater transform in ontologie ,call llm to modify by nlp, help trip extract by video of tiktot
class extraction :
    def __init__(self,obj,state,action):
        self.obj=obj
        self.state = state
        self.action = action



    def update_state(self):
        if self.state == "sO":
            print("that mean agent doen't start yet")
        elif self.state =="s1":
            print("agent start ")
        elif self.state == "s2":
            print("agent stop ")
        else :
            print("it's not compatible with the sate off agent")
    def action_start(self):
        """Start when the action need , and modify the state of the agent to put in start """
        self.state = "s1"

    def action_end(self):
        """end when the action need , and modify the state of the agent to put in end """
        self.state = "s2"
    