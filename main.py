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
            a = node.no_node
            if a is not None:
                node = node.no_node
            else:
                break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


    if node and node.recommendation:
        print("\nRecommendation:", node.recommendation)


root = TreeNode(
    "Do you exercise regularly?",
    yes_node=TreeNode(
        "Do you follow a balanced diet?",
        yes_node=TreeNode(
            "Do you get enough sleep?",
            yes_node=TreeNode(
                "Do you drink alchocol?",
                yes_node=None,
                no_node=None,
                recommendation="You will not die"
            ),
            no_node= TreeNode(
                "Do you drink alchocol?",
                yes_node=None,
                no_node=None,
                recommendation="You will die"
            )
        ),
        no_node=TreeNode(
            "Do you want tips on improving your diet?",
            yes_node=TreeNode(
                "Do you believe me",
                yes_node=None,
                no_node=None,
                recommendation="Consider consulting a nutritionist for personalized advice."
            ),
            no_node=TreeNode(
                "Do you believe me",
                yes_node=None,
                no_node=None,
                recommendation="You will die, stupid loser"
            )
            
        )
    ),
    no_node=TreeNode(
        "Do you want to start an exercise routine?",
        yes_node=TreeNode(
            "Do you believe me",
            yes_node=None,
            no_node=None,
            recommendation="Start with light exercises and gradually increase intensity for better health."
        ),
        no_node=TreeNode(
            "Do you believe me",
            yes_node=None,
            no_node=None,
            recommendation="Die, stupid fat loser"
        )
    )
)

traverse_decision_tree(root)
