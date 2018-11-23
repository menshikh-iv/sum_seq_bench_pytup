#include <Python.h>
#include "sum_seq.h"


static PyObject *sum_seq_sum_seq(PyObject *self, PyObject *args);

static PyMethodDef module_methods[] = {
    {"sum_seq", sum_seq_sum_seq, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "sum_seq",  // module name
    NULL, // module docstring
    -1,
    module_methods,
    NULL,
    NULL,
    NULL,
    NULL,
};

PyObject *PyInit_sum_seq(void){
    PyObject *module = PyModule_Create(&moduledef);
    if (module == NULL)
        return NULL;
    return module;
}

static PyObject *sum_seq_sum_seq(PyObject *self, PyObject *args){
    unsigned long long int n = 0, value = 0;

    if (!PyArg_ParseTuple(args, "K", &n)){
        return NULL;
    }

    Py_BEGIN_ALLOW_THREADS
    value = sum_seq(n);
    Py_END_ALLOW_THREADS

    PyObject *ret = Py_BuildValue("K", value);
    return ret;
}
