#include <stdio.h>
#include <string.h>

#include <CL/cl.h>

int main() {
        char buf[]="Hello, World!";
        char build_c[4096];
        size_t srcsize, worksize=strlen(buf);
        
        cl_int error;
        cl_platform_id platform;
        cl_device_id device;
        cl_uint platforms, devices;
    
        /* Fetch the Platforms, we only want one. */
        error=clGetPlatformIDs(1, &platform, &platforms);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        /* Fetch the Devices for this platform */
        error=clGetDeviceIDs(platform, CL_DEVICE_TYPE_ALL, 1, &device, &devices);
        if (error != CL_SUCCESS) {  
                printf("\n Error number %d", error);
        }
        /* Create a memory context for the device we want to use  */
        cl_context_properties properties[]={CL_CONTEXT_PLATFORM, (cl_context_properties)platform,0};
        /* Note that nVidia's OpenCL requires the platform property */
        cl_context context=clCreateContext(properties, 1, &device, NULL, NULL, &error);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        /* Create a command queue to communicate with the device */
        cl_command_queue cq = clCreateCommandQueue(context, device, 0, &error);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        
        /* Read the source kernel code in exmaple.cl as an array of char's */
        char src[8192];
        FILE *fil=fopen("example.cl","r");
        srcsize=fread(src, sizeof src, 1, fil);
        fclose(fil);
    
        const char *srcptr[]={src};
        /* Submit the source code of the kernel to OpenCL, and create a program object with it */
        cl_program prog=clCreateProgramWithSource(context,
                                              1, srcptr, &srcsize, &error);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }

        /* Compile the kernel code (after this we could extract the compiled version) */
        error=clBuildProgram(prog, 0, NULL, "", NULL, NULL);
        if ( error != CL_SUCCESS ) {
                printf( "Error on buildProgram " );
                printf("\n Error number %d", error);
                fprintf( stdout, "\nRequestingInfo\n" );
                clGetProgramBuildInfo( prog, devices, CL_PROGRAM_BUILD_LOG, 4096, build_c, NULL );
                printf( "Build Log for %s_program:\n%s\n", "example", build_c );
        }
    
        /* Create memory buffers in the Context where the desired Device is. These will be the pointer 
        parameters on the kernel. */
        cl_mem mem1, mem2;
        mem1=clCreateBuffer(context, CL_MEM_READ_ONLY, worksize, NULL, &error);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        mem2=clCreateBuffer(context, CL_MEM_WRITE_ONLY, worksize, NULL, &error);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        /* Create a kernel object with the compiled program */
        cl_kernel k_example=clCreateKernel(prog, "example", &error);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }

        /* Set the kernel parameters */
        error = clSetKernelArg(k_example, 0, sizeof(mem1), &mem1);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        error = clSetKernelArg(k_example, 1, sizeof(mem2), &mem2);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        /* Create a char array in where to store the results of the Kernel */
        char buf2[sizeof buf];
        buf2[0]='?';
        buf2[worksize]=0;
    
        /* Send input data to OpenCL (async, don't alter the buffer!) */
        error=clEnqueueWriteBuffer(cq, mem1, CL_FALSE, 0, worksize, buf, 0, NULL, NULL);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        /* Tell the Device, through the command queue, to execute que Kernel */
        error=clEnqueueNDRangeKernel(cq, k_example, 1, NULL, &worksize, &worksize, 0, NULL, NULL);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        /* Read the result back into buf2 */
        error=clEnqueueReadBuffer(cq, mem2, CL_FALSE, 0, worksize, buf2, 0, NULL, NULL);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        /* Await completion of all the above */
        error=clFinish(cq);
        if (error != CL_SUCCESS) {
                printf("\n Error number %d", error);
        }
        /* Finally, output the result */
        puts(buf2);
}
And this is without printing the names of the error flags, that would add a large function.

Kernel code for both cases in OpenCL C (note that SimpleOpenCL doesn't alter Device code at all)

__kernel void example( __global char* buf, __global char* buf2 ){
       int x = get_global_id(0);

       buf2[x] = buf[x];

}/* Please Write the OpenCL Kernel(s) code here*/
