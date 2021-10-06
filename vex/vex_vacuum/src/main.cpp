/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       main.cpp                                                  */
/*    Author:       VEX                                                       */
/*    Created:      Thu Sep 26 2019                                           */
/*    Description:  Drivetrain With Variables                                 */
/*                                                                            */
/*                  This program demonstrates how to change the speed of a    */
/*                  drivetrain's drive and turn actions.                      */
/*                                                                            */
/*----------------------------------------------------------------------------*/

// ---- START VEXCODE CONFIGURED DEVICES ----
// Robot Configuration:
// [Name]               [Type]        [Port(s)]
// Drivetrain           drivetrain    1, 10, D
// ---- END VEXCODE CONFIGURED DEVICES ----

#include "vex.h"

using namespace vex;

float Distance;

int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();

  // Setting the variable "Distance" to a value of 11
  Distance = 11;
  // Drives the robot forward for 11 inches
  Drivetrain.driveFor(forward, Distance, inches);
}
