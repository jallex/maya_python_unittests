# Unit tests

from maya import cmds
from base import MayaBaseTestCase
import code

class TestJoints(MayaBaseTestCase):
    def setUp(self):
        """Run BEFORE every test_* method.
        
        Notes:
            There is a "tearDown" method as well, which runs AFTER every test.
        """
        super(TestJoints, self).setUp()

        self.joint_name = code.make_joint(position=[1,1,1], name="my_joint0")
        cmds.select(clear=True)
        cmds.select( self.joint_name )
        self.child_joint_name1 = code.make_joint(position=[2.2, 9.34, 6.5], name="my_joint1")
        cmds.select(clear=True)
        cmds.select( self.child_joint_name1 )
        self.child_joint_name2 = code.make_joint(position=[-2.0, 5.09, -3.1], name="my_joint2")

    def test_node_exists(self):
        """Test whether node was actually created."""
        transform_exists = cmds.objExists(self.joint_name)
        self.assertTrue(transform_exists)

    def test_joint_position(self):
        """Test whether joint was created at the correct position."""
        target_pos = [1.0, 1.0, 1.0]
        cmds.select(clear=True)
        cmds.select( self.joint_name )
        selected = cmds.ls(selection=True)[0]
        translate_x_value = cmds.getAttr("%s.translateX" % selected)
        translate_y_value = cmds.getAttr("%s.translateX" % selected)
        translate_z_value = cmds.getAttr("%s.translateX" % selected)
        actual_pos = [translate_x_value, translate_y_value, translate_z_value]
        self.assertEqual(actual_pos, target_pos)

    def test_joint_position_child1(self):
        """Test whether first child joint was created at the correct position."""
        target_pos = [2.2, 9.34, 6.5]
        cmds.select(clear=True)
        cmds.select( self.child_joint_name1 )
        selected = cmds.ls(selection=True)[0]
        translate_x_value = cmds.getAttr("%s.translateX" % selected)
        translate_y_value = cmds.getAttr("%s.translateX" % selected)
        translate_z_value = cmds.getAttr("%s.translateX" % selected)
        actual_pos = [translate_x_value, translate_y_value, translate_z_value]
        self.assertEqual(actual_pos, target_pos)
    
    def test_joint_position_child2(self):
        """Test whether second child joint was created at the correct position."""
        target_pos = [-2.0, 5.09, -3.1]
        cmds.select(clear=True)
        cmds.select( self.child_joint_name2 )
        selected = cmds.ls(selection=True)[0]
        translate_x_value = cmds.getAttr("%s.translateX" % selected)
        translate_y_value = cmds.getAttr("%s.translateX" % selected)
        translate_z_value = cmds.getAttr("%s.translateX" % selected)
        actual_pos = [translate_x_value, translate_y_value, translate_z_value]
        self.assertEqual(actual_pos, target_pos)

    def test_translation(self):
        """Test moving the joint."""
        target_pos = [9.0, 9.0, 9.0]
        #move joint to target
        code.move_joint( self.child_joint_name1, target_pos)
        cmds.select(clear=True)
        cmds.select( self.child_joint_name1 )
        selected = cmds.ls(selection=True)[0]
        translate_x_value = cmds.getAttr("%s.translateX" % selected)
        translate_y_value = cmds.getAttr("%s.translateX" % selected)
        translate_z_value = cmds.getAttr("%s.translateX" % selected)
        actual_pos = [translate_x_value, translate_y_value, translate_z_value]
        self.assertEqual(actual_pos, target_pos)

