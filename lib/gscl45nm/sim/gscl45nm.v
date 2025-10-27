

module AND2X1 (A, B, Y);
input  A ;
input  B ;
output Y ;

   and (Y, A, B);
endmodule
module AND2X2 (A, B, Y);
input  A ;
input  B ;
output Y ;

   and (Y, A, B);


endmodule
module AOI21X1 (A, B, C, Y);
input  A ;
input  B ;
input  C ;
output Y ;

   and (I0_out, A, B);
   or  (I1_out, I0_out, C);
   not (Y, I1_out);


endmodule
module AOI22X1 (C, D, Y, B, A);
input  C ;
input  D ;
input  B ;
input  A ;
output Y ;

   and (I0_out, C, D);
   and (I1_out, A, B);
   or  (I2_out, I0_out, I1_out);
   not (Y, I2_out);


endmodule




module BUFX2 (Y, A);
input  A ;
output Y ;

   buf (Y, A);


endmodule




module BUFX4 (Y, A);
input  A ;
output Y ;

   buf (Y, A);


endmodule




module CLKBUF1 (Y, A);
input  A ;
output Y ;

   buf (Y, A);


endmodule




module CLKBUF2 (A, Y);
input  A ;
output Y ;

   buf (Y, A);


endmodule




module CLKBUF3 (A, Y);
input  A ;
output Y ;

   buf (Y, A);


endmodule




module DFFNEGX1 (Q, CLK, D);
input  CLK ;
input  D ;
output Q ;
reg NOTIFIER ;

   not (I0_CLOCK, CLK);
   udp_dff (DS0000, D, I0_CLOCK, 1'B0, 1'B0, NOTIFIER);
   not (P0000, DS0000);
   buf (Q, DS0000);


endmodule




module DFFPOSX1 (CLK, Q, D);
input  CLK ;
input  D ;
output Q ;
reg NOTIFIER ;

   udp_dff (DS0000, D, CLK, 1'B0, 1'B0, NOTIFIER);
   not (P0000, DS0000);
   buf (Q, DS0000);


endmodule




module DFFSR (CLK, D, S, R, Q);
input  CLK ;
input  D ;
input  S ;
input  R ;
output Q ;
reg NOTIFIER ;

   not (I0_CLEAR, R);
   not (I0_SET, S);
   udp_dff (P0003, D_, CLK, I0_SET, I0_CLEAR, NOTIFIER);
   not (D_, D);
   not (P0002, P0003);
   buf (Q, P0002);
   and (D_EQ_1_AN_S_EQ_1, D, S);
   not (I9_out, D);
   and (D_EQ_0_AN_R_EQ_1, I9_out, R);
   and (S_EQ_1_AN_R_EQ_1, S, R);


endmodule




module FAX1 (YC, B, C, A, YS);
input  B ;
input  C ;
input  A ;
output YC ;
output YS ;

   and (I0_out, A, B);
   and (I1_out, B, C);
   and (I3_out, C, A);
   or  (YC, I0_out, I1_out, I3_out);
   xor (I5_out, A, B);
   xor (YS, I5_out, C);


endmodule




module HAX1 (YS, B, A, YC);
input  B ;
input  A ;
output YS ;
output YC ;

   xor (YS, A, B);
   and (YC, A, B);


endmodule




module INVX1 (A, Y);
input  A ;
output Y ;

   not (Y, A);


endmodule




module INVX2 (A, Y);
input  A ;
output Y ;

   not (Y, A);


endmodule




module INVX4 (Y, A);
input  A ;
output Y ;

   not (Y, A);


endmodule




module INVX8 (A, Y);
input  A ;
output Y ;

   not (Y, A);


endmodule




module LATCH (D, CLK, Q);
input  D ;
input  CLK ;
output Q ;
reg NOTIFIER ;

   udp_tlat (DS0000, D, CLK, 1'B0, 1'B0, NOTIFIER);
   not (P0000, DS0000);
   buf (Q, DS0000);


endmodule




module MUX2X1 (A, Y, S, B);
input  A ;
input  S ;
input  B ;
output Y ;

   udp_mux2 (I0_out, B, A, S);
   not (Y, I0_out);


endmodule




module NAND2X1 (A, B, Y);
input  A ;
input  B ;
output Y ;

   and (I0_out, A, B);
   not (Y, I0_out);


endmodule




module NAND3X1 (A, B, C, Y);
input  A ;
input  B ;
input  C ;
output Y ;

   and (I1_out, A, B, C);
   not (Y, I1_out);


endmodule




module NOR2X1 (A, B, Y);
input  A ;
input  B ;
output Y ;

   or  (I0_out, A, B);
   not (Y, I0_out);


endmodule




module NOR3X1 (A, B, C, Y);
input  A ;
input  B ;
input  C ;
output Y ;

   or  (I1_out, A, B, C);
   not (Y, I1_out);


endmodule




module OAI21X1 (A, B, C, Y);
input  A ;
input  B ;
input  C ;
output Y ;

   or  (I0_out, A, B);
   and (I1_out, I0_out, C);
   not (Y, I1_out);


endmodule




module OAI22X1 (C, D, Y, B, A);
input  C ;
input  D ;
input  B ;
input  A ;
output Y ;

   or  (I0_out, C, D);
   or  (I1_out, A, B);
   and (I2_out, I0_out, I1_out);
   not (Y, I2_out);


endmodule




module OR2X1 (A, B, Y);
input  A ;
input  B ;
output Y ;

   or  (Y, A, B);


endmodule




module OR2X2 (A, B, Y);
input  A ;
input  B ;
output Y ;

   or  (Y, A, B);


endmodule




module TBUFX1 (EN, A, Y);
input  EN ;
input  A ;
output Y ;

   not (I0_out, A);
   bufif1 (Y, I0_out, EN);


endmodule




module TBUFX2 (EN, Y, A);
input  EN ;
input  A ;
output Y ;

   not (I0_out, A);
   bufif1 (Y, I0_out, EN);


endmodule




module XNOR2X1 (B, Y, A);
input  B ;
input  A ;
output Y ;

   xor (I0_out, A, B);
   not (Y, I0_out);


endmodule




module XOR2X1 (B, Y, A);
input  B ;
input  A ;
output Y ;

   xor (Y, A, B);


endmodule


primitive udp_dff (out, in, clk, clr, set, NOTIFIER);
   output out;
   input  in, clk, clr, set, NOTIFIER;
   reg    out;

   table

// in  clk  clr   set  NOT  : Qt : Qt+1
//
   0  r   ?   0   ?   : ?  :  0  ; // clock in 0
   1  r   0   ?   ?   : ?  :  1  ; // clock in 1
   1  *   0   ?   ?   : 1  :  1  ; // reduce pessimism
   0  *   ?   0   ?   : 0  :  0  ; // reduce pessimism
   ?  f   ?   ?   ?   : ?  :  -  ; // no changes on negedge clk
   *  b   ?   ?   ?   : ?  :  -  ; // no changes when in switches
   ?  ?   ?   1   ?   : ?  :  1  ; // set output
   ?  b   0   *   ?   : 1  :  1  ; // cover all transistions on set
   1  x   0   *   ?   : 1  :  1  ; // cover all transistions on set
   ?  ?   1   0   ?   : ?  :  0  ; // reset output
   ?  b   *   0   ?   : 0  :  0  ; // cover all transistions on clr
   0  x   *   0   ?   : 0  :  0  ; // cover all transistions on clr
   ?  ?   ?   ?   *   : ?  :  x  ; // any notifier changed

   endtable
endprimitive // udp_dff

primitive udp_tlat (out, in, enable, clr, set, NOTIFIER);

   output out;
   input  in, enable, clr, set, NOTIFIER;
   reg    out;

   table

// in  enable  clr   set  NOT  : Qt : Qt+1
//
   1  1   0   ?   ?   : ?  :  1  ; //
   0  1   ?   0   ?   : ?  :  0  ; //
   1  *   0   ?   ?   : 1  :  1  ; // reduce pessimism
   0  *   ?   0   ?   : 0  :  0  ; // reduce pessimism
   *  0   ?   ?   ?   : ?  :  -  ; // no changes when in switches
   ?  ?   ?   1   ?   : ?  :  1  ; // set output
   ?  0   0   *   ?   : 1  :  1  ; // cover all transistions on set
   1  ?   0   *   ?   : 1  :  1  ; // cover all transistions on set
   ?  ?   1   0   ?   : ?  :  0  ; // reset output
   ?  0   *   0   ?   : 0  :  0  ; // cover all transistions on clr
   0  ?   *   0   ?   : 0  :  0  ; // cover all transistions on clr
   ?  ?   ?   ?   *   : ?  :  x  ; // any notifier changed

   endtable
endprimitive // udp_tlat

primitive udp_rslat (out, clr, set, NOTIFIER);

   output out;
   input  clr, set, NOTIFIER;
   reg    out;

   table

// clr   set  NOT  : Qt : Qt+1
//
   ?   1   ?   : ?  :  1  ; // set output
   0   *   ?   : 1  :  1  ; // cover all transistions on set
   1   0   ?   : ?  :  0  ; // reset output
   *   0   ?   : 0  :  0  ; // cover all transistions on clr
   ?   ?   *   : ?  :  x  ; // any notifier changed

   endtable
endprimitive // udp_tlat

primitive udp_mux2 (out, in0, in1, sel);
   output out;
   input  in0, in1, sel;

   table

// in0 in1 sel :  out
//
    1  ?  0 :  1 ;
    0  ?  0 :  0 ;
    ?  1  1 :  1 ;
    ?  0  1 :  0 ;
    0  0  x :  0 ;
    1  1  x :  1 ;

   endtable
endprimitive // udp_mux2

