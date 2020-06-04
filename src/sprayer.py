import cv2


nozzle_position = (250, 150)
hole_spacing = 3
spray_dimensions = (1, 1)
spray_color = (255, 0, 255)

sprayer_height = 60

belt_x_vel = 0.7
belt_y_vel = 0

spray_points = []


def queue_spray(box_y):
    holes = []
    for y in box_y:
        if y % hole_spacing == 0:
            hole = y / hole_spacing
            holes.append(hole)
            starting_x = nozzle_position[0] + 0
            starting_y = nozzle_position[1] + y
            spray_points.append(SprayPoint(starting_x, starting_y, 50))


def draw_sprayer(img):
    cv2.rectangle(img, (nozzle_position[0] - 5, nozzle_position[1]-spray_dimensions[1]*2),
                  (nozzle_position[0] + 5, nozzle_position[1] + spray_dimensions[1]*2 + 60), (240, 240, 240), -1)

    cv2.rectangle(img, (nozzle_position[0] - 5, nozzle_position[1]-spray_dimensions[1]*2),
                  (nozzle_position[0] + 5, nozzle_position[1] + spray_dimensions[1]*2 + 60), (20, 20, 20), 1)

    for hole in range(0, int(sprayer_height/hole_spacing)):
        cv2.ellipse(img, (int(nozzle_position[0]), int(nozzle_position[1] + hole * hole_spacing)),
                    (spray_dimensions[0]*2, spray_dimensions[1]*2), 0, 0, 360, (0, 0, 255), -1)


def update(img):
    draw_sprayer(img)

    for spray_point in spray_points:
        if spray_point.is_active():

            cv2.ellipse(img, spray_point.get_pos(), spray_dimensions, 0, 0, 360, spray_color, -1)
            spray_point.tick(belt_x_vel, belt_y_vel)


class SprayPoint:
    def __init__(self, starting_x, starting_y, delay):
        self.x = starting_x
        self.y = starting_y
        self.spray_delay = delay

    def tick(self, x_vel, y_vel):
        self.x += x_vel
        self.y += y_vel

    def get_pos(self):
        return int(self.x), int(self.y)

    def is_active(self):
        if self.spray_delay <= 1:
            return True
        else:
            self.spray_delay -= 1
            return False
