#pragma once
#include "Vetor.h"

class Triangle
{
public:
	int Id;
	float vertices[3][3];		// 3 v�rtices do tri�ngulo
	float normal[3];
	Vetor Normal;
	
public:
	Triangle(int tId, float tvertices[3][3]);
	~Triangle();
};

