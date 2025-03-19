"use strict";

/**
 * @namespace KTSearcher
 */
var KTSearcher = function () {

      /**
       * @function sussessHandler
       * @returns {void}
       * @description
       */
      function sussessHandler() {
        $('.city-select2').on('change', function() {
           let selectedValue = $(this).val();

            // Construye la URL
            let redirectTo = URL_ATRACCIONES + selectedValue;

            // Redirecciona al navegador
            window.location.href = redirectTo;
        });

      }

    /**
     * @function init
     * @returns {void}
     */
    function init() {

        $(document).ready(function() {
            $('.city-select2').select2({
                placeholder: "Seleccione un pais",
                allowClear: true
            });
        });
        sussessHandler();



    }

    return {
        init: init
    }
}();

// Inicializar KTSearcher una vez que el DOM esté completamente cargado.
document.addEventListener("DOMContentLoaded", function () {
    KTSearcher.init();
});
