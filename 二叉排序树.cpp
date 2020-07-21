#include<stdio.h>
#include<stdlib.h>
#define MAXSIZE 10
typedef struct BiTree {
	int Element;
	struct BiTree* left;
	struct BiTree* right;
};
typedef struct BiTree* Tree;

bool SearchBST(Tree root, int element, Tree f, Tree& p)
{
	if (!root)
	{
		p = f;
		return false;
	}
	else if (root->Element == element)
	{
		p = root;
		return true;
	}
	else if (element < root->Element)
	{
		return SearchBST(root->left, element, root, p);
	}
	else 
	{
		return SearchBST(root->right, element, root, p);
	}
}

void InsertBST(Tree& root, int element)
{
	Tree p, s;
	if (!SearchBST(root, element, NULL, p))
	{
		s = (Tree)malloc(sizeof(BiTree));
		s->Element = element;
		s->left = s->right = NULL;
		if (!p)
		{
			root = s;
		}
		else if (element < p->Element)
		{
			p->left = s;
		}
		else
		{
			p->right = s;
		}
		return;
	}
	else
	{
		return;
	}
}

bool Delete(Tree& p)
{
	Tree q, s;
	if (p->right == NULL)
	{
		q = p;
		p = p->left;
		free(q);
	}
	else if (p->left == NULL)
	{
		q = p;
		p = p->right;
		free(q);
	}
	else
	{
		q = p;
		s = p->left;
		while (s->right)
		{
			q = s;
			s = s->right;
		}
		p->Element = s->Element;
		if (q!= p)
		{
			q->right = s->left;
		}
		else
		{
			q->left = s->left;
		}
		free(s);
	}
	return true;
}

bool DeleteBST(Tree& root, int element)
{
	if (!root)
	{
		return false;
	}
	else
	{
		if (root->Element == element)
		{
			return Delete(root);
		}
		else if (element < root->Element)
		{
			return DeleteBST(root->left, element);
		}
		else if (element > root->Element)
		{
			return DeleteBST(root->right, element);
		}
	}
}

void InOrderBST(Tree root)
{
	if (root)
	{
		InOrderBST(root->left);
		printf("%d\t", root->Element);
		InOrderBST(root->right);
	}
}

int main()
{
	Tree root = NULL;
	int* a = (int*)malloc(MAXSIZE * sizeof(int));
	int count = 0;
	while (1)
	{
		scanf_s("%d", a + count);
		if (a[count] == 0)
			break;
		InsertBST(root, a[count]);
		count++;
	}
	InOrderBST(root);
	return 0;
}