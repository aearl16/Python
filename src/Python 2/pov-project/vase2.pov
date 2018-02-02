/*
CS360 Lab 1
@Author: Aaron Earl
Vase
*/

#include "colors.inc"
#include "glass.inc"

global_settings { ambient_light White }

camera{ location <6,6,6> look_at <0,0,0>}

light_source 
{
    <50,50,50>  //Source Location  
    color White*2 //Doubles Brightness
}

//Set a background color
background { color White }

//Create a "floor"
plane 
{
  <0,1,0>, 0 //This represents the plane 0x+0y+z=0
  pigment {color Grey*0.15}
}

#declare mybox = box
{
    <-1,0,-1><1,0.25,1> //Cube with thickness .1
    pigment {rgb <0.9,0,0>} //Solid Red 
    texture
    {
        pigment { Red filter 0.75}
        finish { F_Glass3 }
    }
}        

#declare loc = <0,1,0>;

#declare ball = sphere
{
  loc, 0.35
      texture
    {
        pigment { White filter 0.95}
        finish { F_Glass3 }
    }
}

#declare ball_light = light_source 
{
    loc  //Source Location  
    color White //Doubles Brightness
}     

ball
ball_light


//Construct a square-based pyramid by intersecting its planes

//Define the coordinates of the five vertices
//<x,y,z>
//#declare plane1 = plane {<2,2,1>,1};    //x+y+z=0 moved 1 unit
//#declare plane2 = plane {<2,-2,1>,1};   //x-y+z=0 moved 1 unit
//#declare plane3 = plane {<-2,2,1>,1};   //-1+y+z=0 moved 1 unit
//#declare plane4 = plane {<-2,-2,1>,1};  //-x-y+z=0 moved 1 unit
//#declare plane5 = plane {<0,0,-1>,0};   //0x+0y-z=0 moved 1 unit

#declare plane1 = plane {<2,1,2>,1};    //x+y+z=0 moved 1 unit
#declare plane2 = plane {<2,1,-2>,1};   //x-y+z=0 moved 1 unit
#declare plane3 = plane {<-2,1,2>,1};   //-1+y+z=0 moved 1 unit
#declare plane4 = plane {<-2,1,-2>,1};  //-x-y+z=0 moved 1 unit
#declare plane5 = plane {<0,-1,0>,0};   //0x+0y-z=0 moved 1 unit

//Define the pyramid to be the intersection of its faces.
#declare mypyramid = object 
{ 
    intersection 
    {
        object{plane1}
        object{plane2} 
        object{plane3} 
        object{plane4} 
        object{plane5}
    }
    texture
    {
        pigment { Red filter 0.95}
        finish { F_Glass3 }
    }
    rotate <180,0,0>
    translate <0,3.1,0>
};

//Display the pyramid
//mypyramid

/*
//Playing with Union function
union 
{
    box { <-1.5, -1, -1>, <0.5, 1, 1> }
    cylinder { <0.5, 0, -1>, <0.5, 0, 1>, 1 }
}
*/

#declare vaseStart = union
{
    object {mypyramid}
    object {mybox} //Cube with thickness .1
}
 
//Display the unioned vase pieces 
vaseStart
//To add another pyramid that uses difference to make a the hollow portion of the vase




