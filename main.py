class TreeNode:
    def __init__(self, question, yes_node, no_node, recommendation=None):
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node
        self.recommendation = recommendation

def traverse_decision_tree(node):
    while True:
        print(node.question)
        answer = input("Enter 'yes' or 'no': ").lower()
        if answer == 'yes':
            a = node.yes_node
            if a is not None:
                node = node.yes_node
            else:
                break
        elif answer == 'no':
            node = node.no_node
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


    if node and node.recommendation:
        print("\nRecommendation:", node.recommendation)




# Define the decision tree structure
root = TreeNode(
    "Do you exercise regularly?",
    yes_node=TreeNode(
        "Do you follow a balanced diet?",
        yes_node=TreeNode(
            "Do you get enough sleep?",
            yes_node=None,
            no_node=None,
            recommendation="You're on the right track! Keep it up!"
        ),
        no_node=TreeNode(
            "Do you want tips on improving your diet?",
            yes_node=None,
            no_node=None,
            recommendation="Consider consulting a nutritionist for personalized advice."
        )
    ),
    no_node=TreeNode(
        "Do you want to start an exercise routine?",
        yes_node=None,
        no_node=None,
        recommendation="Start with light exercises and gradually increase intensity for better health."
    )
)

# Traverse the decision tree based on user responses
traverse_decision_tree(root)
