module AFIFO(wclk, wrstn, wren, wdata, wfull,rclk, rrstn, rden, rdata, rempty);
parameter dsize = 8,
asize = 4;
localparam dw = dsize,
           aw = asize;
input wire wclk, wrstn, wren;
input wire [dw-1:0] wdata;
output	reg wfull;
input	wire rclk, rrstn, rden;
output	wire	[dw-1:0] rdata;
output	reg	rempty;

wire [aw-1:0] waddrmem, raddrmem;
wire wfull_next, rempty_next;
reg [aw:0] wgray, wbin, wq2_rgray, wq1_rgray,rgray, rbin, rq2_wgray, rq1_wgray;
				
	
wire [aw:0] wgraynext, wbinnext;
wire [aw:0] rgraynext, rbinnext;

reg [dw-1:0]	mem	[0:((1<<aw)-1)];

	
initial	{ wq2_rgray,  wq1_rgray } = 0;
always @(posedge wclk or negedge wrstn)
 if (!wrstn)
   { wq2_rgray, wq1_rgray } <= 0;
else { wq2_rgray, wq1_rgray } <= { wq1_rgray, rgray };

assign	wbinnext  = wbin + { {(aw){1'b0}}, ((wren) && (!wfull)) };
assign	wgraynext = (wbinnext >> 1) ^ wbinnext;

assign	waddrmem = wbin[aw-1:0];

initial	{ wbin, wgray } = 0;
always @(posedge wclk or negedge wrstn)
if (!wrstn)
	{ wbin, wgray } <= 0;
else
{ wbin, wgray } <= { wbinnext, wgraynext };

assign	wfull_next = (wgraynext == { ~wq2_rgray[aw:aw-1],wq2_rgray[aw-2:0] });

				
initial	wfull = 0;
always @(posedge wclk or negedge wrstn)
 if (!wrstn)
    wfull <= 1'b0;
	else
	wfull <= wfull_next;

always @(posedge wclk)
if ((wren)&&(!wfull))
	mem[waddrmem] <= wdata;

initial	{ rq2_wgray,  rq1_wgray } = 0;
always @(posedge rclk or negedge rrstn)
if (!rrstn)
 { rq2_wgray, rq1_wgray } <= 0;
else
{ rq2_wgray, rq1_wgray } <= { rq1_wgray, wgray };


assign	rbinnext  = rbin + { {(aw){1'b0}}, ((rden)&&(!rempty)) };
assign	rgraynext = (rbinnext >> 1) ^ rbinnext;

initial	{ rbin, rgray } = 0;
	always @(posedge rclk or negedge rrstn)
if (!rrstn)
	{ rbin, rgray } <= 0;
else
	{ rbin, rgray } <= { rbinnext, rgraynext };

assign	raddrmem = rbin[aw-1:0];
assign	rempty_next = (rgraynext == rq2_wgray);
initial rempty = 1;
always @(posedge rclk or negedge rrstn)
if (!rrstn)
	rempty <= 1'b1;
else
	rempty <= rempty_next;

assign	rdata = mem[raddrmem];
endmodule