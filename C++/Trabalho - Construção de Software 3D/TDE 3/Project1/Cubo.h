#pragma once

class Cubo
{
public:
	float pcx, pcy, pcz;
	float a;            // Aresta
	int id;
    float f1[4][3];
    float f2[4][3];
    float f3[4][3];     // Faces
    float f4[4][3];     // do Cubo
    float f5[4][3];
    float f6[4][3];

	Cubo(int idC, float ppcx, float ppcy, float ppcz, float aa);
	void Desenha();
	~Cubo();
};