module readtest;
	reg bit[0:8];
	reg[7:0] mem[0:256];

	integer i, j;

	integer allzero = 1;
	integer receiving = 1;
	integer waitingforack = 0;

	integer memidx = 0;

	always #1 begin
		if(receiving == 1) begin
			$readmemb("input.hex", bit);

			if(bit[0] == 1) begin
				allzero = 1;
				$display("time=%d", $realtime);

				for (i = 1; i < 9; i = i + 1) begin
					if(allzero == 1 && bit[i] != 0) begin
						allzero = 0; 
					end
				  
					$display("%d", bit[i]);
					mem[memidx][i-1] = bit[i];
				end
				
				bit[0] = 0;
				$writememb("input.hex", bit);
				memidx = memidx + 1;

				if(allzero == 1) begin
					receiving = 0;	  
					waitingforack = 0;
					$display("EOF");
				end
			end
		end
		else begin
		  	$display("talking %d words", memidx);
		  	for(j = 0; j < memidx - 1; j = j + 1) begin
			  	$display("t");
				if(waitingforack == 0) begin
				  	$display("putting");
					bit[0] = 0;
					for(i = 1; i < 9; i = i + 1) begin
						bit[i] = mem[j][i-1];
					end
					$writememb("input.hex", bit);
					$display("waiting for ack");

					waitingforack = 1;
				  	while(waitingforack == 1) begin
						$readmemb("input.hex", bit);
						if(bit[0] == 1) begin
							waitingforack = 0;
							$display("ack received");
						end
						
					end
				end
			end

			for(i = 0; i < 9; i = i + 1) begin
				bit[i] = 0;
			end
			$writememb("input.hex", bit);
			memidx = 0;
			receiving = 1;
		end
	end
endmodule
