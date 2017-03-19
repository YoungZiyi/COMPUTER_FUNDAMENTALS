#include <stdio.h>
#include <stdlib.h>
/**
 *
 * 使用链表实现多项式的表示及其操作
 *
 */

typedef struct polyNode *polyNodePtr;
struct polyNode {
    int coef;
    int expon;
    polyNodePtr next;
};


void printPoly(polyNodePtr p)
{
    while (p)
    {
        printf("coef: %d expon: %d\n", p->coef, p->expon);
        p = p->next;
    }
}

polyNodePtr createPoly(void)
{
    polyNodePtr node;
    node = malloc(sizeof(node));
    return node;
}

void attach(int coef, int expon, polyNodePtr *p)
{
    polyNodePtr temp;
    temp = malloc(sizeof(temp));
    
    temp->coef = coef;
    temp->expon = expon;

    (*p)->next = temp;
    (*p) = temp;
}

polyNodePtr polyAdd(polyNodePtr a, polyNodePtr b)
{
    polyNodePtr c, tail, zeroNode;
    tail = malloc(sizeof(tail));
    c = tail;

    int sum;

    while (a && b)
    {
        if (a->expon == b->expon)
        {
            sum = a->coef + b->coef;
            if (sum)
                attach(sum, a->expon, &tail);

            a = a->next;
            b = b->next;
        }
        else if (a->expon > b->expon)
        {
            attach(a->coef, a->expon, &tail);
            
            a = a->next;
        }
        else
        {
            attach(b->coef, b->expon, &tail);

            b = b->next;
        }
    }
    
    for (; a; a = a->next) attach(a->coef, a->expon, &tail);
    for (; b; b = b->next) attach(b->coef, b->expon, &tail);

    tail->next = NULL;

    zeroNode = c;
    c = c->next;
    free(zeroNode);

    return c;
}



int main()
{
    polyNodePtr head1, tail;
    tail = createPoly();
    head1 = tail;
    attach(2,2,&tail);
    printf("head1 is :\n");
    printPoly(head1);

    polyNodePtr head2, tail2;
    tail2 = createPoly();
    head2 = tail2;
    attach(3,3,&tail2);
    printf("head2 is :\n");
    printPoly(head2);

    printf("\nhead_sum is:\n");

    polyNodePtr head_sum;
    head_sum = polyAdd(head1, head2);

    printPoly(head_sum);
    
    return 0;
}
