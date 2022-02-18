// Gabriel Farias | TDE 1
#include "colors.inc"
#include "textures.inc"    
#include "stars.inc" 
camera {
    perspective angle 70 //angulo camera
    location  <0 , 1 ,-50>  
    look_at   <0 , 2 , 0>
}
sphere{ <0,0,0>, 1  //Essa esfera cria um background/skybox com uma textura 
        texture{ Starfield1 } // Textura para o Skybox 
        scale 10000 
        rotate<clock,0,0>   // A rotação no eixo X faz a textura rotacionar dando animação
} 

plane { // Plano da cena
    <0,-1,0>,1 
    texture{ Silver_Metal
    finish { phong 1 }
    scale 0.5
    }  
}   
                     
#declare Figura = union { // Declaração da figura principal
difference{ //Diferença subtrai do cone 2 partes em um formato de torus 
cone {  // Cone que tem duas extrusões no formato de 2 toros  
<0,0,0>,0.75,<0,1.50,0>,0 
texture {Gold_Metal finish { phong 1 reflection{ 0.1 metallic 0.00} }} //Cone
       scale <5,5,5> 
       rotate<0,0,0> 
       translate<0,2,-30>         
     }
torus { 1.0,0.25 // 1ro torus substraido do cone  
        texture {Silver1 finish { phong 1 reflection { 0.25 metallic 1} }} 
        scale <2,2,2> 
        rotate<0,0,0> 
        translate<0,6,-30>
     }
torus { 0.5,0.25// 2do torus subtraido do cone 
        texture {Silver1 finish { phong 1 reflection { 0.25 metallic 1} }} 
        scale <2,2,2> 
        rotate<0,0,0> 
        translate<0,8,-30>
     }
} // Fim da operação da difference | subtração de área
torus { 3,0.1 // 1to torus que faz o anel da figura
        texture {Silver1 finish { phong 1 reflection { 0.5 metallic 1} }} 
        scale <2,2,2> 
        rotate<clock,clock,0> // faz com que rotacione o eixo x e y num sentido diagonal 
        translate<0,6,-30>
     }              
torus { 3.3,0.1  // 2do torus que faz o anel da figura
        texture {Silver1 finish { phong 1 reflection { 0.5 metallic 1} }} 
        scale <2,2,2> 
        rotate<-clock,-clock,0> // faz com que rotacione todavia com o clock negativo faz com que se vá na direção oposta ao torus anterior
        translate<0,6,-30>
     }  
text { 
    ttf "arial.ttf", "GabWorks", 0.2, 0.0 // Texto 3d
       texture{ Silver2 finish { phong 0.1 }} 
       scale<2,2.5,2>
       translate<-4.5,4,-33 >
      }
}
light_source { // Luz de área geral, faz com que as sombras projetem
  <0,0,0>             
  color rgb 1.0       
  area_light
  <8, 0, 0> <0, 0, 8> 
  4, 4                
  adaptive 5         
  jitter              
  circular            
  orient              
  translate <40, 80, -40>   
}
light_source {  // Luz spotlight Azul embaixo da Figura
  <0,5,-30>                 
  color rgb <50,50,255>       
  spotlight               
  translate <0, 10, 100> 
  point_at <0, 5, -30>      
  radius 5              
  tightness 20        
  falloff 15             
} 
light_source {  // Luz de ponto amarela que faz os aneis (torus brilharem)
  0                 
  color rgb <255,255,0>    
  translate <0, 1, -20>
}    
Figura  // Chamada da figura

 





