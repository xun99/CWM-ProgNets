/* -*- P4_16 -*- */
#include <core.p4>
#include <v1model.p4>

/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/

typedef bit<9>  egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ip4Addr_t;
const bit<16> TYPE_AUTOTRADER = ;

header ethernet_t {
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<16>   etherType;
}

/*header ipv4_t {
    ip4Addr_t dstAddr;
    ip4Addr_t scrAddr;
}*/

header autotrader_t {
    bit<32> order;
}

struct metadata {
    /* empty */
}

struct headers {
    ethernet_t   ethernet;
    /*ipv4_t       ipv4;*/
    autotrader_t autotrader;
}

register<bit<32>>(1) R1;

/*************************************************************************
*********************** P A R S E R  ***********************************
*************************************************************************/

parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                inout standard_metadata_t standard_metadata) {

    state start {
        packet.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType) {
            TYPE_AUTOTRADER: parse_autotrader;
            default: accept;
        }
    state parse_autotrader {
    	packet.extract(hdr.autotrader);
    	transition accept;
    }
    
    }

}


/*************************************************************************
************   C H E C K S U M    V E R I F I C A T I O N   *************
*************************************************************************/

control MyVerifyChecksum(inout headers hdr, inout metadata meta) {   
    apply {  }
}


/*************************************************************************
**************  I N G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyIngress(inout headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {

    /*
    action swap_mac_addresses() {
       macAddr_t tmp_mac;
       tmp_mac = hdr.ethernet.dstAddr;
       hdr.ethernet.dstAddr = hdr.ethernet.srcAddr;
       hdr.ethernet.srcAddr = tmp_mac;

       //send it back to the same port
       standard_metadata.egress_spec = standard_metadata.ingress_port;
    }
    */
    
    action drop() {
        mark_to_drop(standard_metadata);
    }
    
    action buy_at_asking_price() {
    	temp = temp + 1;
    }
    
    action sell_at_bidding_price() {
        temp = temp - 1;
    }
    
    apply {
    	bit<32> temp;
    	R1.read(temp,0);
        if () {
            if (hdr.autotrader.order == "bid") {
            	sell_at_bidding_price();
            }
            if (hdr.autotrader.order == "ask") {
                buy_at_asking_price();
            }
        }
        R1.write(0,temp);
    }
}
       
       
    


/*************************************************************************
****************  E G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyEgress(inout headers hdr,
                 inout metadata meta,
                 inout standard_metadata_t standard_metadata) {
    apply {  }
}

/*************************************************************************
*************   C H E C K S U M    C O M P U T A T I O N   **************
*************************************************************************/

control MyComputeChecksum(inout headers hdr, inout metadata meta) {
     apply {

     }
}


/*************************************************************************
***********************  D E P A R S E R  *******************************
*************************************************************************/

control MyDeparser(packet_out packet, in headers hdr) {
    apply {
        packet.emit(hdr.ethernet);
    }
}

/*************************************************************************
***********************  S W I T C H  *******************************
*************************************************************************/

V1Switch(
MyParser(),
MyVerifyChecksum(),
MyIngress(),
MyEgress(),
MyComputeChecksum(),
MyDeparser()
) main;
