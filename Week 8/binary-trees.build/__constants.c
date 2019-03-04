
#include "nuitka/prelude.h"
#include "structseq.h"

// Sentinel PyObject to be used for all our call iterator endings. It will
// become a PyCObject pointing to NULL. It's address is unique, and that's
// enough for us to use it as sentinel value.
PyObject *_sentinel_value = NULL;

PyObject *Nuitka_dunder_compiled_value = NULL;

PyObject *const_int_0;
PyObject *const_str_dot;
PyObject *const_int_pos_1;
PyObject *const_str_empty;
PyObject *const_dict_empty;
PyObject *const_tuple_empty;
PyObject *const_str_plain_rb;
PyObject *const_str_plain_int;
PyObject *const_str_plain_len;
PyObject *const_str_plain_sum;
PyObject *const_str_plain_iter;
PyObject *const_str_plain_long;
PyObject *const_str_plain_name;
PyObject *const_str_plain_open;
PyObject *const_str_plain_read;
PyObject *const_str_plain_repr;
PyObject *const_str_plain_site;
PyObject *const_str_plain_type;
PyObject *const_str_plain_level;
PyObject *const_str_plain_range;
PyObject *const_str_plain_format;
PyObject *const_str_plain_locals;
PyObject *const_str_plain_xrange;
PyObject *const_str_plain___all__;
PyObject *const_str_plain___cmp__;
PyObject *const_str_plain___doc__;
PyObject *const_str_plain_compile;
PyObject *const_str_plain_globals;
PyObject *const_str_plain_inspect;
PyObject *const_str_plain___dict__;
PyObject *const_str_plain___exit__;
PyObject *const_str_plain___file__;
PyObject *const_str_plain___iter__;
PyObject *const_str_plain___main__;
PyObject *const_str_plain___name__;
PyObject *const_str_plain___path__;
PyObject *const_str_plain_exc_type;
PyObject *const_str_plain_fromlist;
PyObject *const_str_plain___class__;
PyObject *const_str_plain___enter__;
PyObject *const_str_plain_bytearray;
PyObject *const_str_plain_exc_value;
PyObject *const_str_plain___import__;
PyObject *const_str_plain___module__;
PyObject *const_str_plain___delattr__;
PyObject *const_str_plain___getattr__;
PyObject *const_str_plain___package__;
PyObject *const_str_plain___setattr__;
PyObject *const_str_plain_classmethod;
PyObject *const_str_plain___builtins__;
PyObject *const_str_plain___compiled__;
PyObject *const_str_plain_staticmethod;
PyObject *const_str_plain___metaclass__;
PyObject *const_str_plain_exc_traceback;
PyObject *const_str_digest_91d422fd0021a0acd73277db22fcb218;
PyObject *const_str_digest_bbf6d4497597e588c1898c426771cc5e;

static void _createGlobalConstants( void )
{
    NUITKA_MAY_BE_UNUSED PyObject *exception_type, *exception_value;
    NUITKA_MAY_BE_UNUSED PyTracebackObject *exception_tb;

#ifdef _MSC_VER
    // Prevent unused warnings in case of simple programs, the attribute
    // NUITKA_MAY_BE_UNUSED doesn't work for MSVC.
    (void *)exception_type; (void *)exception_value; (void *)exception_tb;
#endif

    const_int_0 = PyInt_FromLong( 0l );
    const_str_dot = UNSTREAM_CHAR( 46, 0 );
    const_int_pos_1 = PyInt_FromLong( 1l );
    const_str_empty = UNSTREAM_STRING( &constant_bin[ 0 ], 0, 0 );
    const_dict_empty = _PyDict_NewPresized( 0 );
    assert( PyDict_Size( const_dict_empty ) == 0 );
    const_tuple_empty = PyTuple_New( 0 );
    const_str_plain_rb = UNSTREAM_STRING( &constant_bin[ 274 ], 2, 1 );
    const_str_plain_int = UNSTREAM_STRING( &constant_bin[ 249 ], 3, 1 );
    const_str_plain_len = UNSTREAM_STRING( &constant_bin[ 276 ], 3, 1 );
    const_str_plain_sum = UNSTREAM_STRING( &constant_bin[ 279 ], 3, 1 );
    const_str_plain_iter = UNSTREAM_STRING( &constant_bin[ 282 ], 4, 1 );
    const_str_plain_long = UNSTREAM_STRING( &constant_bin[ 11 ], 4, 1 );
    const_str_plain_name = UNSTREAM_STRING( &constant_bin[ 286 ], 4, 1 );
    const_str_plain_open = UNSTREAM_STRING( &constant_bin[ 290 ], 4, 1 );
    const_str_plain_read = UNSTREAM_STRING( &constant_bin[ 294 ], 4, 1 );
    const_str_plain_repr = UNSTREAM_STRING( &constant_bin[ 298 ], 4, 1 );
    const_str_plain_site = UNSTREAM_STRING( &constant_bin[ 302 ], 4, 1 );
    const_str_plain_type = UNSTREAM_STRING( &constant_bin[ 306 ], 4, 1 );
    const_str_plain_level = UNSTREAM_STRING( &constant_bin[ 310 ], 5, 1 );
    const_str_plain_range = UNSTREAM_STRING( &constant_bin[ 315 ], 5, 1 );
    const_str_plain_format = UNSTREAM_STRING( &constant_bin[ 320 ], 6, 1 );
    const_str_plain_locals = UNSTREAM_STRING( &constant_bin[ 326 ], 6, 1 );
    const_str_plain_xrange = UNSTREAM_STRING( &constant_bin[ 332 ], 6, 1 );
    const_str_plain___all__ = UNSTREAM_STRING( &constant_bin[ 338 ], 7, 1 );
    const_str_plain___cmp__ = UNSTREAM_STRING( &constant_bin[ 345 ], 7, 1 );
    const_str_plain___doc__ = UNSTREAM_STRING( &constant_bin[ 352 ], 7, 1 );
    const_str_plain_compile = UNSTREAM_STRING( &constant_bin[ 359 ], 7, 1 );
    const_str_plain_globals = UNSTREAM_STRING( &constant_bin[ 366 ], 7, 1 );
    const_str_plain_inspect = UNSTREAM_STRING( &constant_bin[ 373 ], 7, 1 );
    const_str_plain___dict__ = UNSTREAM_STRING( &constant_bin[ 380 ], 8, 1 );
    const_str_plain___exit__ = UNSTREAM_STRING( &constant_bin[ 388 ], 8, 1 );
    const_str_plain___file__ = UNSTREAM_STRING( &constant_bin[ 396 ], 8, 1 );
    const_str_plain___iter__ = UNSTREAM_STRING( &constant_bin[ 404 ], 8, 1 );
    const_str_plain___main__ = UNSTREAM_STRING( &constant_bin[ 412 ], 8, 1 );
    const_str_plain___name__ = UNSTREAM_STRING( &constant_bin[ 420 ], 8, 1 );
    const_str_plain___path__ = UNSTREAM_STRING( &constant_bin[ 428 ], 8, 1 );
    const_str_plain_exc_type = UNSTREAM_STRING( &constant_bin[ 436 ], 8, 1 );
    const_str_plain_fromlist = UNSTREAM_STRING( &constant_bin[ 444 ], 8, 1 );
    const_str_plain___class__ = UNSTREAM_STRING( &constant_bin[ 452 ], 9, 1 );
    const_str_plain___enter__ = UNSTREAM_STRING( &constant_bin[ 461 ], 9, 1 );
    const_str_plain_bytearray = UNSTREAM_STRING( &constant_bin[ 470 ], 9, 1 );
    const_str_plain_exc_value = UNSTREAM_STRING( &constant_bin[ 479 ], 9, 1 );
    const_str_plain___import__ = UNSTREAM_STRING( &constant_bin[ 488 ], 10, 1 );
    const_str_plain___module__ = UNSTREAM_STRING( &constant_bin[ 498 ], 10, 1 );
    const_str_plain___delattr__ = UNSTREAM_STRING( &constant_bin[ 508 ], 11, 1 );
    const_str_plain___getattr__ = UNSTREAM_STRING( &constant_bin[ 519 ], 11, 1 );
    const_str_plain___package__ = UNSTREAM_STRING( &constant_bin[ 530 ], 11, 1 );
    const_str_plain___setattr__ = UNSTREAM_STRING( &constant_bin[ 541 ], 11, 1 );
    const_str_plain_classmethod = UNSTREAM_STRING( &constant_bin[ 552 ], 11, 1 );
    const_str_plain___builtins__ = UNSTREAM_STRING( &constant_bin[ 563 ], 12, 1 );
    const_str_plain___compiled__ = UNSTREAM_STRING( &constant_bin[ 575 ], 12, 1 );
    const_str_plain_staticmethod = UNSTREAM_STRING( &constant_bin[ 587 ], 12, 1 );
    const_str_plain___metaclass__ = UNSTREAM_STRING( &constant_bin[ 599 ], 13, 1 );
    const_str_plain_exc_traceback = UNSTREAM_STRING( &constant_bin[ 612 ], 13, 1 );
    const_str_digest_91d422fd0021a0acd73277db22fcb218 = UNSTREAM_STRING( &constant_bin[ 625 ], 49, 0 );
    const_str_digest_bbf6d4497597e588c1898c426771cc5e = UNSTREAM_STRING( &constant_bin[ 674 ], 92, 0 );

#if _NUITKA_EXE
    /* Set the "sys.executable" path to the original CPython executable. */
    PySys_SetObject(
        (char *)"executable",
        const_str_digest_bbf6d4497597e588c1898c426771cc5e
    );

    /* Set the "sys.executable" path to the original CPython executable. */
    PySys_SetObject(
        (char *)"prefix",
        const_str_digest_91d422fd0021a0acd73277db22fcb218
    );

#endif

    static PyTypeObject Nuitka_VersionInfoType;

    // Same fields as "sys.version_info" except no serial number.
    static PyStructSequence_Field Nuitka_VersionInfoFields[] = {
        {(char *)"major", (char *)"Major release number"},
        {(char *)"minor", (char *)"Minor release number"},
        {(char *)"micro", (char *)"Micro release number"},
        {(char *)"releaselevel", (char *)"'alpha', 'beta', 'candidate', or 'release'"},
        {0}
    };

    static PyStructSequence_Desc Nuitka_VersionInfoDesc = {
        (char *)"__nuitka_version__",                                    /* name */
        (char *)"__compiled__\n\nVersion information as a named tuple.", /* doc */
        Nuitka_VersionInfoFields,                                        /* fields */
        4
    };

    PyStructSequence_InitType(&Nuitka_VersionInfoType, &Nuitka_VersionInfoDesc);

    Nuitka_dunder_compiled_value = PyStructSequence_New(&Nuitka_VersionInfoType);
    assert(Nuitka_dunder_compiled_value != NULL);

    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 0, PyInt_FromLong(0));
    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 1, PyInt_FromLong(6));
    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 2, PyInt_FromLong(2));

#if PYTHON_VERSION < 300
    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 3, PyString_FromString("release"));
#else
    PyStructSequence_SET_ITEM(Nuitka_dunder_compiled_value, 3, PyUnicode_FromString("release"));
#endif
    // Prevent users from creating the Nuitka version type object.
    Nuitka_VersionInfoType.tp_init = NULL;
    Nuitka_VersionInfoType.tp_new = NULL;


}

// In debug mode we can check that the constants were not tampered with in any
// given moment. We typically do it at program exit, but we can add extra calls
// for sanity.
#ifndef __NUITKA_NO_ASSERT__
void checkGlobalConstants( void )
{

}
#endif

void createGlobalConstants( void )
{
    if ( _sentinel_value == NULL )
    {
#if PYTHON_VERSION < 300
        _sentinel_value = PyCObject_FromVoidPtr( NULL, NULL );
#else
        // The NULL value is not allowed for a capsule, so use something else.
        _sentinel_value = PyCapsule_New( (void *)27, "sentinel", NULL );
#endif
        assert( _sentinel_value );

        _createGlobalConstants();
    }
}
