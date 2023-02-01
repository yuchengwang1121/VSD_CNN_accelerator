if {![namespace exists ::IMEX]} { namespace eval ::IMEX {} }
set ::IMEX::dataVar [file dirname [file normalize [info script]]]
set ::IMEX::libVar ${::IMEX::dataVar}/libs

create_library_set -name lib_typ\
   -timing\
    [list ${::IMEX::libVar}/mmmc/fsa0m_a_generic_core_tt1p8v25c.lib\
    ${::IMEX::libVar}/mmmc/fsa0m_a_t33_generic_io_tt1p8v25c.lib\
    ${::IMEX::libVar}/mmmc/SRAM_TC.lib\
    ${::IMEX::libVar}/mmmc/data_array_TC.lib\
    ${::IMEX::libVar}/mmmc/tag_array_TC.lib\
    ${::IMEX::libVar}/mmmc/SUMA180_384X32X1BM4_TC.lib\
    ${::IMEX::libVar}/mmmc/SUMA180_32768X16X1BM8_TC.lib\
    ${::IMEX::libVar}/mmmc/SUMA180_16384X18X1BM4_TC.lib]\
   -si\
    [list ${::IMEX::libVar}/mmmc/u18_tt.cdb]
create_library_set -name lib_min\
   -timing\
    [list ${::IMEX::libVar}/mmmc/fsa0m_a_generic_core_ff1p98vm40c.lib\
    ${::IMEX::libVar}/mmmc/fsa0m_a_t33_generic_io_ff1p98vm40c.lib\
    ${::IMEX::libVar}/mmmc/SRAM_BC.lib\
    ${::IMEX::libVar}/mmmc/data_array_BC.lib\
    ${::IMEX::libVar}/mmmc/tag_array_BC.lib\
    ${::IMEX::libVar}/mmmc/SUMA180_384X32X1BM4_BC.lib\
    ${::IMEX::libVar}/mmmc/SUMA180_32768X16X1BM8_BC.lib\
    ${::IMEX::libVar}/mmmc/SUMA180_16384X18X1BM4_BC.lib]\
   -si\
    [list ${::IMEX::libVar}/mmmc/u18_ff.cdb]
create_library_set -name lib_max\
   -timing\
    [list ${::IMEX::libVar}/lib/typ/fsa0m_a_generic_core_ss1p62v125c.lib\
    ${::IMEX::libVar}/lib/typ/fsa0m_a_t33_generic_io_ss1p62v125c.lib\
    ${::IMEX::libVar}/lib/typ/SRAM_WC.lib\
    ${::IMEX::libVar}/lib/typ/data_array_WC.lib\
    ${::IMEX::libVar}/lib/typ/tag_array_WC.lib\
    ${::IMEX::libVar}/lib/typ/SUMA180_384X32X1BM4_WC.lib\
    ${::IMEX::libVar}/lib/typ/SUMA180_32768X16X1BM8_WC.lib\
    ${::IMEX::libVar}/lib/typ/SUMA180_16384X18X1BM4_WC.lib]\
   -si\
    [list ${::IMEX::libVar}/mmmc/u18_ss.cdb]
create_rc_corner -name RC\
   -cap_table ${::IMEX::libVar}/mmmc/u18_Faraday.CapTbl\
   -preRoute_res 1\
   -postRoute_res 1\
   -preRoute_cap 1\
   -postRoute_cap 1\
   -postRoute_xcap 1\
   -preRoute_clkres 0\
   -preRoute_clkcap 0
create_delay_corner -name DC_typ\
   -library_set lib_typ\
   -rc_corner RC
create_delay_corner -name DC_min\
   -library_set lib_min\
   -rc_corner RC
create_delay_corner -name DC_max\
   -library_set lib_max\
   -rc_corner RC
create_constraint_mode -name CM\
   -sdc_files\
    [list ${::IMEX::libVar}/mmmc/APR.sdc]
create_analysis_view -name AV_max -constraint_mode CM -delay_corner DC_max
create_analysis_view -name AV_typ -constraint_mode CM -delay_corner DC_typ
create_analysis_view -name AV_min -constraint_mode CM -delay_corner DC_min
set_analysis_view -setup [list AV_max AV_typ] -hold [list AV_min]
