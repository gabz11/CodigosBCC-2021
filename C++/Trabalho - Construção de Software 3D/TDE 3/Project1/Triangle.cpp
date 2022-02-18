#include <math.h>
#include "Triangle.h"

Triangle::Triangle(int tId, float tvertices[3][3])
{
	Id = tId;
	vertices[0][0] = tvertices[0][0];  // v�rtice 0 coord x
	vertices[0][1] = tvertices[0][1];  // v�rtice 0 coord y
	vertices[0][2] = tvertices[0][2];  // v�rtice 0 coord z
	vertices[1][0] = tvertices[1][0];
	vertices[1][1] = tvertices[1][1];
	vertices[1][2] = tvertices[1][2];
	vertices[2][0] = tvertices[2][0];
	vertices[2][1] = tvertices[2][1];
	vertices[2][2] = tvertices[2][2];

	Vetor v1(0, 0, 0, 0), v2(0, 0, 0, 0);

    v1.xcomp = vertices[0][0] - vertices[1][0];
    v1.ycomp = vertices[0][1] - vertices[1][1];
    v1.zcomp = vertices[0][2] - vertices[1][2];

    v2.xcomp = vertices[2][0] - vertices[1][0];
    v2.ycomp = vertices[2][1] - vertices[1][1];
    v2.zcomp = vertices[2][2] - vertices[1][2];

    Normal = Normal.ProdutoVetorial(v1, v2);
    Normal.Normalizar();
}


Triangle::~Triangle()
{
}
