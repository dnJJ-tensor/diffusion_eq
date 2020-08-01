      !f2py --fcompiler=gfortran -m (Python)のモジュール名 -c twodscalor_Euler_explc.f90

      subroutine twodscalor_Euler_explc(Phi_in, Dx, Dy, nx ,ny, Phi_hist)
        
      implicit none
        real(8)    :: Dx, Dy
        integer    :: nx, ny
        real(8)    :: Phi_in(nx, ny)
        real(8)    :: Phi_cal(nx, ny)
        real(8)    :: Phi_hist(nx, ny)
        integer    :: i, j
      intent(in)::Phi_in
      intent(in):: Dx, Dy
      intent(in):: nx, ny 
      intent(out)::Phi_hist

      Phi_cal(:,:) = Phi_in(:,:)
      Phi_hist(:,:)= Phi_in(:,:)
      
       !y方向:ディレクレ条件
       !x方向:ディレクレ条件      

          do i = 2, nx-1
              do j = 2, ny-1
                  Phi_hist(i,j)  =   Phi_cal(i, j) &
                            + Dx*(Phi_cal(i+1,j) -2*Phi_cal(i,j) + Phi_cal(i-1,j))&
                            + Dy*(Phi_cal(i,j+1) -2*Phi_cal(i,j) + Phi_cal(i,j-1))
              end do
          end do
          
          !ノイマン条件を設定するには以下をコメントアウトしないでコンパイル
          !x=0
          !Phi_hist(1:nx,1) = Phi_hist(1:nx,2)
          !x=nx
          !Phi_hist(1:nx,ny) = Phi_hist(1:nx,ny-1)
          !y=0
          !Phi_hist(1,1:ny) = Phi_hist(2,1:ny)
          !y=ny
          !Phi_hist(nx,1:ny) = Phi_hist(nx-1,1:ny)

      end subroutine twodscalor_Euler_explc