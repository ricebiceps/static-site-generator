from textnode import(
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new.append(old_node)
            continue
        partitions = old_node.text.spilt(delimiter)
        if len(temp) % 2 == 0:
            raise Exception("no closing delimiter")
        for i in range(len(partitions)):
            if partitions[i] == "":
                continue
            if i % 2 == 0:
                new.append(TextNode(partition[i],text_type_text))
            else:
                new.append(TextNode(partition[i],text_type))    
    return new
