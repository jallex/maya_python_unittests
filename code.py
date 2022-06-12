"""Joint module."""
from maya import cmds

def make_joint(position, name):
    """Create a joint at given position with given name
    Args:
        position (list [float, float, float]): Position for the joint
        name (str): Name for the joint to be created.
    Returns:
        joint: newly created joint
    """
    # Create joint based on position and name
    cmds.select( d=True )
    joint = cmds.joint( p=position, n=name )
    return joint

def add_to_joint_chain(position, name, parent_name):
    """Create a joint at given position with given name, and parented to the given parent joint name
    Args:
        position (list [float, float, float]): position for the joint
        name (str): Name for the joint to be created.
        parent_name (str): the name of the parent joint
    Returns:
        joint: newly created joint
    """
    # In the creation mode, a new joint will be created as a child of a selected 
    # transform or starts a hierarchy by itself if no transform is selected.
    # get currently selected object

    # clear selection
    cmds.select(clear=True)
    cmds.select( parent_name )
    # Create joint based on position and name
    joint = cmds.joint( p=position, n=name )
    return joint

def move_joint(joint_name, new_position):
    """Move given joint by name to a new position
    Args:
        joint_name (str): Name of hte joint we want to move
        new_position (list [float, float, float]): new position for the joint
    Returns:
        new_position: the new position of the joint
    """
    cmds.select(clear=True)
    cmds.select( joint_name )
    cmds.joint( e=True, p=new_position)
    return new_position
