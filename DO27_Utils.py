import numpy as np
import matplotlib.pyplot as plt

def getSlice(sigma,mesh,sliceInd,normal):
    v = mesh.r(sigma,'CC','CC','M')
    if   normal == 'X': sigmaSlice = v[sliceInd,:,:]
    elif normal == 'Y': sigmaSlice = v[:,sliceInd,:]
    elif normal == 'Z': sigmaSlice = v[:,:,sliceInd]

    h2d = []
    x2d = []
    if 'X' not in normal:
        h2d.append(mesh.hx)
        x2d.append(mesh.x0[0])
    if 'Y' not in normal:
        h2d.append(mesh.hy)
        x2d.append(mesh.x0[1])
    if 'Z' not in normal:
        h2d.append(mesh.hz)
        x2d.append(mesh.x0[2])
    mesh2D = mesh.__class__(h2d, x2d) #: Temp Mesh

    return sigmaSlice, mesh2D

def getBlkOutline(trueMod,mesh,sliceInd,normal, ax, color='k'):

    from scipy.stats import mode

    secMat,secMesh = getSlice(trueMod,mesh,sliceInd,normal)
    secVec = secMesh.r(secMat,'CC','CC','V')

    modGrad = secMesh.cellGrad*secVec

    TargetF_Ind = np.where(np.abs(modGrad) > 0)[0]

    if(len(TargetF_Ind) != 0):

        if(normal == 'X'):
            gridFy = secMesh.gridFx
            gridFz = secMesh.gridFy

            dy_core = mode(secMesh.hx)[0]
    #         print(dy_core)
            dz_core = mode(secMesh.hy)[0]
    #         print(dz_core)

            targetFy_Ind = []
            targetFz_Ind = []
            for ind in TargetF_Ind:
                if(ind <= secMesh.nFx):
                    targetFy_Ind.append(ind)
                else:
                    targetFz_Ind.append(ind - secMesh.nFx)

            targetFy = gridFy[targetFy_Ind,:]
            targetFz = gridFz[targetFz_Ind,:]

            for ii in range(0,targetFy.shape[0]):
                start = np.array([targetFy[ii,0], targetFy[ii,1] - (dz_core/2.)])
                end = np.array([targetFy[ii,0], targetFy[ii,1] + (dz_core/2.)])
                ax.plot(np.array([start[0], end[0]]), np.array([start[1], end[1]]), linestyle = 'dashed',linewidth = 2.,color=color)

            for jj in range(0,targetFz.shape[0]):
                start = np.array([targetFz[jj,0] - (dy_core/2.), targetFz[jj,1]])
                end = np.array([targetFz[jj,0] + (dy_core/2.), targetFz[jj,1]])
                ax.plot(np.array([start[0], end[0]]), np.array([start[1], end[1]]), linestyle = 'dashed',linewidth = 2.,color=color)

        if(normal == 'Y'):
            gridFx = secMesh.gridFx
            gridFz = secMesh.gridFy

            dx_core = mode(secMesh.hx)[0]
    #         print(dx_core)
            dz_core = mode(secMesh.hy)[0]
    #         print(dz_core)

            targetFx_Ind = []
            targetFz_Ind = []
            for ind in TargetF_Ind:
                if(ind <= secMesh.nFx):
                    targetFx_Ind.append(ind)
                else:
                    targetFz_Ind.append(ind - secMesh.nFx)

            targetFx = gridFx[targetFx_Ind,:]
        #     print(targetFx)
            targetFz = gridFz[targetFz_Ind,:]

            for ii in range(0,targetFx.shape[0]):
                start = np.array([targetFx[ii,0], targetFx[ii,1] - (dz_core/2.)])
                end = np.array([targetFx[ii,0], targetFx[ii,1] + (dz_core/2.)])
                ax.plot(np.array([start[0], end[0]]), np.array([start[1], end[1]]), linestyle = 'dashed',linewidth = 2.,color=color)

            for jj in range(0,targetFz.shape[0]):
                start = np.array([targetFz[jj,0] - (dx_core/2.), targetFz[jj,1]])
                end = np.array([targetFz[jj,0] + (dx_core/2.), targetFz[jj,1]])
                ax.plot(np.array([start[0], end[0]]), np.array([start[1], end[1]]), linestyle = 'dashed',linewidth = 2.,color=color)

        if(normal == 'Z'):
            gridFx = secMesh.gridFx
            gridFy = secMesh.gridFy

            dx_core = mode(secMesh.hx)[0]
    #         print(dx_core)
            dy_core = mode(secMesh.hy)[0]
    #         print(dy_core)

            targetFx_Ind = []
            targetFy_Ind = []
            for ind in TargetF_Ind:
                if(ind <= secMesh.nFx):
                    targetFx_Ind.append(ind)
                else:
                    targetFy_Ind.append(ind - secMesh.nFx)

            targetFx = gridFx[targetFx_Ind,:]
            targetFy = gridFy[targetFy_Ind,:]

            for ii in range(0,targetFx.shape[0]):
                start = np.array([targetFx[ii,0], targetFx[ii,1] - (dy_core/2.)])
                end = np.array([targetFx[ii,0], targetFx[ii,1] + (dy_core/2.)])
                ax.plot(np.array([start[0], end[0]]), np.array([start[1], end[1]]), linestyle = 'dashed',linewidth = 2.,color=color)

            for jj in range(0,targetFy.shape[0]):
                start = np.array([targetFy[jj,0] - (dx_core/2.), targetFy[jj,1]])
                end = np.array([targetFy[jj,0] + (dx_core/2.), targetFy[jj,1]])
                ax.plot(np.array([start[0], end[0]]), np.array([start[1], end[1]]), linestyle = 'dashed',linewidth = 2.,color=color)
