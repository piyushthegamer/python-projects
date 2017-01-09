/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

    $(document).ready(function() {                                

        $("#btn").click(function(e){
                    $(this).hide();
                    $("#name").hide();
                    $('#name_edit').removeClass('hidden');
                    $('#ok').removeClass('hidden');
                   e.preventDefault();
                });
        $("#ok").click(function(f){

                    $("#btn").show();
                    $("#name").show();
                    $('#name_edit').addClass('hidden');
                    $('#ok').addClass('hidden');                     
        });                
    });
        
