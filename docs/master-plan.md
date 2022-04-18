# Master Plan

When I was about 7 years old, I recieved an voice controlled R2-D2 interactive toy robot as a gift from my Grandpa, which I've kept ever since.
Almost 19 years later, this is my plan to overhaul his guts and make him into a fully customizable, programmable robot.

## General Goals

Before I can plan/design high-level tasks for R2 to perform, I kinda need to design his low-level systems.

But in general, I want R2 to have the following functionality:

* Responds to voice commands for interactivity.
* Self-locomotion. The ability to navigate the environment intelligently would also be cool.
* Sound like R2D2 from Official Star Wars media.
* Easily programmable. Software for R2 can be written elsewhere and uploaded to his internal systems for ease of execution.

## Overview

My general idea for this project is to replace the main circuit board (R2's brain, so to speak) with a Raspberry Pi (RPI, for short), running custom R2-D2 software of my own design. The RPI would be re-integrated with as many of R2's original hardware components as possible, such his various motors and sensors.

## Discrete Challenges

We can break up this project into multiple challenges that can be tackled independently:

* Hardware:
  * Understanding the original circuitry and hardware. In order to successfully connect the original hardware with the main board, I need to know the components work.
  * Powering R2. Originally, R2 required 4 D batteries and 4 AA batteries to function. I'd rather R2 be rechargable, so as not to burn through batteries. Additionally, I need to figure out how to power the RPI using whatever solution I come up with.
* Software:
  * R2 needs to be able to convert speech to text for command processing.
  * Audio playback of R2-D2 sound effects.
  * Code for common functions is required (movement of the wheels, turning his head, etc).
  * Shared libraries of R2-D2's generic functionality, to make coding of new programs easier.
  * A method of installing new programs to R2 will be necessary.
