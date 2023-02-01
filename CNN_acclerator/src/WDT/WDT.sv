module WDT (
    input clk,
    input rst,
    input clk2,
    input rst2,
    input WDEN,
    input WDLIVE,
    input [31:0] WTOCNT,
    output logic WTO
);
    logic [31:0]count;
    logic wden,wden_temp,wdlive;
    logic [31:0]wtocnt;
    logic wdlive1;
    logic [31:0]wtocnt1;
    logic wdlive2;
    logic [31:0]wtocnt2;
    logic wdlive3;
    logic [31:0]wtocnt3;
    logic wdlive4;
     
    always_ff@(posedge clk2) begin
        if(rst2) begin
            wden_temp <= 1'b0;
            wden <= 1'b0;
        end
        else begin
            wden_temp <= WDEN;
		    wden <= wden_temp;
        end
    end
    logic [2:0]cont;
    always_ff @(posedge clk) begin
		if(rst) begin
			wdlive <= 1'b0;
			cont <= 3'b0;
			wtocnt <= 32'b0;
		end
            else begin 
			if(cont==3'b111) begin 
				wdlive <= wdlive ^ WDLIVE;
				wtocnt <= WTOCNT;
				cont <= 3'b0;
			end
			else cont <= cont+3'b1;
		end
    end
    
    always_ff @(posedge clk2) begin
		if(rst2) begin		
		    wdlive1 <= 1'b0;            
		    wdlive2 <= 1'b0;
            wdlive3 <= 1'b0;
            wdlive4 <= 1'b0;

            
            wtocnt1 <= 32'b0;
            wtocnt2 <= 32'b0;
            wtocnt3 <= 32'b0;
		end
		else begin 
		    wdlive1 <= wdlive;            
		    wdlive2 <= wdlive1;
            wdlive3 <= wdlive2;
            wdlive4 <= wdlive3 ^ wdlive2;

        
            wtocnt1 <= wtocnt; 
            wtocnt2 <= wtocnt1;
            wtocnt3 <= wtocnt2;
		end
		
    end
    always_ff @(posedge clk2) begin
        if(rst2) begin
            count <= 32'b0;
            WTO <= 1'b0;
        end
        else if(wden == 1) begin
            if(count < wtocnt3) begin
                if(wdlive4 == 1) count <= 32'b0;
                else count <= count +32'b1;
                WTO <= 0; 
            end
            else begin 
                count <= 32'b0;
                WTO <= 1;
            end
        end
    end
endmodule
