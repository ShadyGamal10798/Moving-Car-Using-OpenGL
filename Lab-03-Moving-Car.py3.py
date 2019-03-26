from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_XYZ():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex(0, 0, 0)
    glVertex(10, 0, 0)

    glColor3f(0, 1, 0)
    glVertex(0, 0, 0)
    glVertex(0, 10, 0)

    glColor3f(0, 0, 1)
    glVertex(0, 0, 0)
    glVertex(0, 0, 10)
    glEnd()


def myInit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 1, 30)
    gluLookAt(8, 9, 10,
              0, 1, 0,
              0, 1, 0)

    glClearColor(1, 1, 1, 1)


angle = 0
x = 0
forward = True


def draw():
    global angle
    global x
    global forward

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    # draw_XYZ()

    glColor3f(.6, .9, 1)
    glBegin(GL_QUADS)
    glVertex(5000, -20.25, -61)
    glVertex(-5000, 221.25, -60)
    glVertex(-3000, -123.25, -60)
    glVertex(-3000, -13.25, 51)
    glEnd()


    glLoadIdentity()
    glColor3f(.2, .2, .2)
    glBegin(GL_POLYGON)
    glVertex(10, 0, 3)
    glVertex(10, 0, -1.5)
    glVertex(-25, 0, -1.5)
    glVertex(-20, 0, 3)
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(6, 0, .7)
    glVertex(4, 0, .7)
    glVertex(4, 0, 1.2)
    glVertex(6, 0, 1.2)

    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(9, 0, .7)
    glVertex(7, 0, .7)
    glVertex(7, 0, 1.2)
    glVertex(9, 0, 1.2)

    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(3, 0, .7)
    glVertex(1, 0, .7)
    glVertex(1, 0, 1.2)
    glVertex(3, 0, 1.2)

    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(0, 0, .7)
    glVertex(-2, 0, .7)
    glVertex(-2, 0, 1.2)
    glVertex(0, 0, 1.2)

    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(-3, 0, .7)
    glVertex(-5, 0, .7)
    glVertex(-5, 0, 1.2)
    glVertex(-3, 0, 1.2)

    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(-6, 0, .7)
    glVertex(-8, 0, .7)
    glVertex(-8, 0, 1.2)
    glVertex(-6, 0, 1.2)

    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(-9, 0, .7)
    glVertex(-11, 0, .7)
    glVertex(-11, 0, 1.2)
    glVertex(-9, 0, 1.2)

    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(-12, 0, .7)
    glVertex(-14, 0, .7)
    glVertex(-14, 0, 1.2)
    glVertex(-12, 0, 1.2)

    glEnd()
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(-15, 0, .7)
    glVertex(-17, 0, .7)
    glVertex(-17, 0, 1.2)
    glVertex(-15, 0, 1.2)

    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex(10, 0, 3)
    glVertex(10, 0, -1.5)
    glVertex(-25, 0, -1.5)
    glVertex(-20, 0, 3)

    glEnd()

    glColor3f(.8, 0, 0)
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)


    glLoadIdentity()
    glColor3f(.6, 0, .1)
    glTranslate(x, 5*0.25, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glColor3f(0, 0, 1)
    glLoadIdentity()
    glTranslate(x+0.5*5, -0.5 * 0.25*5, 0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x+0.5*5, -0.5 * 0.25*5, - 0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x-0.5*5, -0.5 * 0.25*5, -0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)

    glLoadIdentity()
    glTranslate(x-0.5*5, -0.5 * 0.25*5, 0.5 * 0.5*5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 10, 10)



    glutSwapBuffers()

    if forward:
        angle -= 0.1
        x += 0.002
        if x > 5:
            forward = False
    else:
        angle += 0.1
        x -= 0.002
        if x < -5:
            forward = True


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
