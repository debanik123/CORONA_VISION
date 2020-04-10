    #!/usr/bin/env python
     
    import sys
    try:
    	#PyGtk library import
     	import pygtk
      	pygtk.require("3.0")
    except:
      	pass
    try:
    	import gtk
      	import gtk.glade
    except:
    	sys.exit(1)
    #ROS related initializations
    import roslib; roslib.load_manifest('ros_glade')
    import rospy
    import os
    from std_msgs.msg import String
    class HellowWorldGTK:
    	def __init__(self):
    		#Set the path to Glade file, in the ros_glade ROS package
    		str=roslib.packages.get_pkg_dir('ros_glade')+"/nodes/ROS_Button.glade"
    		self.gladefile = str 
    		#Initiate the Builder and point it to the glade file
    		self.builder = gtk.Builder()
    		self.builder.add_from_file(self.gladefile)
    		#Connect event functions
    		self.builder.connect_signals(self)
    		self.pub = rospy.Publisher('chatter', String)
    	    	rospy.init_node('talker')
    	def SendButton_cliked(self, widget):
    		#Simple button cliked event
    		self.talker() #Calls talker function which sends a ROS message
            	print "You clicked the button"
    	def talker(self):
    	    	#ROS message hello world
    	    if not rospy.is_shutdown():
    		str = "hello world %s"%rospy.get_time()
    		rospy.loginfo(str)
    		self.pub.publish(String(str))
    	def Timer1_timeout(self):
    		#Timer functions that sends ROS messages every second
    		self.talker()
    		return 1
    	def MainWindow_destroy(self,widget):
    		#MainWindow_destroy event
    		sys.exit(0)
    if __name__ == "__main__":
    	#start the class
    	hwg = HellowWorldGTK()
    	gtk.timeout_add(1000, hwg.Timer1_timeout) #Adds a timer to the GUI, with hwg.Timer1_timeout as a 
    	#callback function for the timer1
    	gtk.main()#Starts GTK


