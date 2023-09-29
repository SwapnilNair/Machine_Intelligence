import numpy as np


class Tensor:

    """
    Tensor Wrapper for Numpy arrays.
    Implements some binary operators.
    Array Broadcasting is disabled
    Args:
        arr: Numpy array (numerical (int, float))
        requires_grad: If the tensor requires_grad (bool)(otherwise gradient dont apply to the tensor)
    """
    def __init__(self, arr, requires_grad=True):

        self.arr = arr
        self.requires_grad = requires_grad
        self.history = ['leaf', None, None]
        self.zero_grad()
        self.shape = self.arr.shape

    def zero_grad(self):
        """
        Set grad to zero
        """
        self.grad = np.zeros_like(self.arr)

    def set_history(self, op, operand1, operand2):
        """
        Set History of the node, indicating how the node was created.
        Ex:-
            history -> ['add', operand1(tensor), operand2(tensor)]
            history -> ['leaf', None, None] if tensor created directly
        Args:
            op: {'add', 'sub', 'mul', 'pow', 'matmul', 'leaf') (str)
            operand1: First operand to the operator. (Tensor object)
            operand2: Second operand to the operator. (Tensor object)
        """
        self.history = list()]
        self.history.append(op)
        self.requires_grad = False
        self.history.append(operand1);self.history.append(operand2)

        if (operand1.requires_grad or operand2.requires_grad):
            self.requires_grad = True

    """
    Addition Operation
    Tensor-Tensor(Element Wise)
    __add__: Invoked when left operand of + is Tensor
    grad_add: Gradient computation through the add operation
    """

    def __add__(self, other):
        """
        Args:
            other: The second operand.(Tensor)
                    Ex: a+b then other -> b, self -> a
        Returns:
            Tensor: That contains the result of operation
        """
        if(isinstance(other, self.__class__)):
            if(self.shape != other.shape):
                raise ArithmeticError(
                    f"Shape mismatch for +: '{self.shape}' and '{other.shape}' ")
            out = self.arr + other.arr
            out_tensor = Tensor(out)
            out_tensor.set_history('add', self, other)

        else:
            raise TypeError(
                f"unsupported operand type(s) for +: '{self.__class__}' and '{type(other)}'")
        return out_tensor

    """
    Matrix Multiplication Operation (@)
    Tensor-Tensor
    __matmul__: Invoked when left operand of @ is Tensor
    grad_matmul: Gradient computation through the matrix multiplication operation
    """

    def __matmul__(self, other):
        """
        Args:
            other: The second operand.(Tensor)
                    Ex: a+b then other -> b, self -> a
        Returns:
            Tensor: That contains the result of operation
        """
        if(not isinstance(other, self.__class__)):
            raise TypeError(
                f"unsupported operand type(s) for matmul: '{self.__class__}' and '{type(other)}'")
        if(self.shape[-1] != other.shape[-2]):
            raise ArithmeticError(
                f"Shape mismatch for matmul: '{self.shape}' and '{other.shape}' ")
        out = self.arr @ other.arr
        out_tensor = Tensor(out)
        out_tensor.set_history('matmul', self, other)

        return out_tensor

    def grad_add(self, gradients=None):
        """
        Find gradients through add operation
        gradients: Gradients from successing operation. (numpy float/int)
        Returns:
            Tuple: (grad1, grad2)
            grad1: Numpy Matrix or Vector(float/int) -> Represents gradients passed to first operand
            grad2: Numpy Matrix or Vector(float/int) -> Represents gradients passed to second operand
            Ex:
                c = a+b
                Gradient to a and b
        """
        if(np.array_equal(self.history[1].arr,self.history[2].arr)):
            return (np.full(self.shape,2),np.full(self.shape,2))

        return (np.full(self.shape,1),np.full(self.shape,1))

    def grad_matmul(self, gradients=None):
        """
        Find gradients through matmul operation
        gradients: Gradients from successing operation. (numpy float/int)
        Returns:
            Tuple: (grad1, grad2)
            grad1: Numpy Matrix or Vector(float/int) -> Represents gradients passed to first operand
            grad2: Numpy Matrix or Vector(float/int) -> Represents gradients passed to second operand
            Ex:
                c = a@b
                Gradients to a and b
        """
        g1=np.matmul(np.full(self.history[1].shape,1),np.transpose(self.history[2].arr))
        g2=np.matmul(np.transpose(self.history[1].arr),np.full(self.history[2].shape,1))

        return (g1,g2)

    def backward(self, gradients=None):
        """
        Backward Pass until leaf node.
        Setting the gradient of which is the partial derivative of node(Tensor) 
        the backward in called on wrt to the leaf node(Tensor).
        Ex:
            a = Tensor(..) #leaf
            b = Tensor(..) #leaf
            c = a+b
            c.backward()
            computes:
                dc/da -> Store in a.grad if a requires_grad
                dc/db -> Store in b.grad if b requires_grad
        Args:
            gradients: Gradients passed from succeeding node
        Returns:
            Nothing. (The gradients of leaf have to set in their respective attribute(leafobj.grad))
        """
        if(self.history[0]!='leaf'):
            ret_val=self.grad_add(gradients) 
        if(self.history[0]=='add' :
        
        else:
            self.grad_matmul(gradients) 
        
        if self.history[0]=='matmul':
        
        else:
            print("Invalid operation")
        gradients=ret_val 
        if gradients==None 
        else:
            (np.multiply(ret_val[0],gradients[0]),np.multiply(ret_val[1],gradients[1]))

            if self.history[1].requires_grad:
                self.history[1].grad=gradients[0]

            if self.history[2].requires_grad:
                self.history[2].grad=gradients[1]

            self.history[1].backward((gradients[0],gradients[0]))

            self.history[2].backward((gradients[1],gradients[1]))
        
        else:
            return
