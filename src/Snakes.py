# Name define:     https://developer-archive.leapmotion.com/documentation/v2/python/devguide/Leap_Overview.html
# APIs references: https://developer-archive.leapmotion.com/documentation/v2/python/api/Leap_Classes.html

import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap

class SampleListener(Leap.Listener):

  def on_connect(self, controller):
    print "Connected"

  def on_frame(self, controller):
    frame = controller.frame()

    hand = frame.hands.rightmost
    position = hand.palm_position
    velocity = hand.palm_velocity
    direction = hand.direction

    if len(frame.hands) > 0:
      for hand in frame.hands:
        for finger in hand.fingers:
          bone_m = finger.bone(Leap.Bone.TYPE_METACARPAL)
          basis_m = bone_m.basis
          m_x_basis = basis_m.x_basis
          m_y_basis = basis_m.y_basis
          m_z_basis = basis_m.z_basis
          m_origin = basis_m.origin
          m_direction = bone_m.direction

          bone_p = finger.bone(Leap.Bone.TYPE_PROXIMAL)
          basis_p = bone_p.basis
          p_x_basis = basis_p.x_basis
          p_y_basis = basis_p.y_basis
          p_z_basis = basis_p.z_basis
          p_origin = basis_p.origin
          p_direction = bone_p.direction

          bone_i = finger.bone(Leap.Bone.TYPE_INTERMEDIATE)
          basis_i = bone_i.basis
          i_x_basis = basis_i.x_basis
          i_y_basis = basis_i.y_basis
          i_z_basis = basis_i.z_basis
          i_origin = basis_i.origin
          i_direction = bone_i.direction

          bone_d = finger.bone(Leap.Bone.TYPE_DISTAL)
          basis_d = bone_d.basis
          d_x_basis = basis_d.x_basis
          d_y_basis = basis_d.y_basis
          d_z_basis = basis_d.z_basis
          d_origin = basis_d.origin
          d_direction = bone_d.direction

          if hand.is_left:
            if finger.type == Leap.Finger.TYPE_THUMB:
              print "Thumb Left: "
            if finger.type == Leap.Finger.TYPE_INDEX:
              print "Index Left: "
            if finger.type == Leap.Finger.TYPE_MIDDLE:
              print "Middle Left: "
            if finger.type == Leap.Finger.TYPE_RING:
              print "Ring Left: "
            if finger.type == Leap.Finger.TYPE_PINKY:
              print "Pinky Left: "
          elif hand.is_right:
            if finger.type == Leap.Finger.TYPE_THUMB:
              print "Thumb Right: "
            if finger.type == Leap.Finger.TYPE_INDEX:
              print "Index Right: "
            if finger.type == Leap.Finger.TYPE_MIDDLE:
              print "Middle Right: "
            if finger.type == Leap.Finger.TYPE_RING:
              print "Ring Right: "
            if finger.type == Leap.Finger.TYPE_PINKY:
              print "Pinky Right: "

          self.print_help("METACARPAL", m_x_basis, m_y_basis, m_z_basis, m_origin, m_direction)
          self.print_help("PROXIMAL", p_x_basis, p_y_basis, p_z_basis, p_origin, p_direction)
          self.print_help("INTERMEDIATE", i_x_basis, i_y_basis, i_z_basis, i_origin, i_direction)
          self.print_help("DISTAL", d_x_basis, d_y_basis, d_z_basis, d_origin, d_direction)
    else:
      print "no hand exist."

  def print_help(self, name, x, y, z, o, d):
    print "----- %s -----" % name
    print "- sides of the finger          x=%8.5f y=%8.5f z=%8.5f" % (x[0], x[1], x[2])
    print "- top and bottom of the finger x=%8.5f y=%8.5f z=%8.5f" % (y[0], y[1], y[2])
    print "- base of the finger           x=%8.5f y=%8.5f z=%8.5f" % (z[0], z[1], z[2])
    print "- origin ???                   x=%8.5f y=%8.5f z=%8.5f" % (o[0], o[1], o[2])
    print "- direction ???                x=%8.5f y=%8.5f z=%8.5f" % (d[0], d[1], d[2])

def main():
  listener = SampleListener()
  controller = Leap.Controller()

  # Have the sample listener receive events from the controller
  controller.add_listener(listener)

  # Keep this process running until Enter is pressed
  print "Press Enter to quit..."
  try:
    sys.stdin.readline()
  except KeyboardInterrupt:
    pass
  finally:
    controller.remove_listener(listener)

if __name__ == "__main__":
  main()