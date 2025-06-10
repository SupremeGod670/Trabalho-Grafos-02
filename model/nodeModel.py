from enum import Enum

class NodeType(Enum):
    ACTOR = "Actor"
    MOVIE = "Movie"


class NodeModel :
    def __init__(self, node_id: int, node_type: NodeType, name: str):
        self.node_id = node_id
        self.node_type = node_type
        self.name = name

    def __repr__(self):
        return f"Node(node_id={self.node_id}, node_type={self.node_type}, name={self.name})"

    def __eq__(self, other):
        if not isinstance(other, NodeType):
            return False
        return (self.node_id == other.node_id and
                self.node_type == other.node_type and
                self.name == other.name)
