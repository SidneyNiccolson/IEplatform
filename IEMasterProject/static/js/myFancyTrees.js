glyph_opts = {
    map: {
      doc: "glyphicon glyphicon-file",
      docOpen: "glyphicon glyphicon-file",
      checkbox: "glyphicon glyphicon-unchecked",
      checkboxSelected: "glyphicon glyphicon-check",
      checkboxUnknown: "glyphicon glyphicon-share",
      dragHelper: "glyphicon glyphicon-play",
      dropMarker: "glyphicon glyphicon-arrow-right",
      error: "glyphicon glyphicon-warning-sign",
      expanderClosed: "glyphicon glyphicon-menu-right",
      expanderLazy: "glyphicon glyphicon-menu-right",  // glyphicon-plus-sign
      expanderOpen: "glyphicon glyphicon-menu-down",  // glyphicon-collapse-down
      folder: "glyphicon glyphicon-folder-close",
      folderOpen: "glyphicon glyphicon-folder-open",
      loading: "glyphicon glyphicon-refresh glyphicon-spin"
    }
  };
  $(function(){
    // Initialize Fancytree
    $("#tree2").fancytree({
      extensions: ["dnd", "edit", "glyph", "wide", "childcounter", "filter"],
      checkbox: true,
      dnd: {
        focusOnClick: true,
        dragStart: function(node, data) { return true; },
        dragEnter: function(node, data) { return false; },
        dragDrop: function(node, data) { data.otherNode.copyTo(node, data.hitMode); }
      },
      glyph: glyph_opts,




      selectMode: 3,
      quicksearch: true,

      source: {{ countryDataReady|safe }},
      filter: {
        autoApply: true,  // Re-apply last filter if lazy data is loaded
        counter: true,  // Show a badge with number of matching child nodes near parent icons
        fuzzy: false,  // Match single characters in order, e.g. 'fb' will match 'FooBar'
        hideExpandedCounter: true,  // Hide counter badge, when parent is expanded
        highlight: true,  // Highlight matches by wrapping inside <mark> tags
        mode: "dimm"  // Grayout unmatched nodes (pass "hide" to remove unmatched node instead)
      },

      toggleEffect: { effect: "drop", options: {direction: "left"}, duration: 400 },
      wide: {
        iconWidth: "1em",     // Adjust this if @fancy-icon-width != "16px"
        iconSpacing: "0.5em", // Adjust this if @fancy-icon-spacing != "3px"
        levelOfs: "1.5em"     // Adjust this if ul padding != "16px"
      },

      icon: function(event, data){
        // if( data.node.isFolder() ) {
        //   return "glyphicon glyphicon-book";
        // }
      },
      childcounter: {
        deep: true,
        hideZeros: true,
        hideExpanded: true
      },

       activate: function(event, data) {
      },


      lazyLoad: function(event, data) {
        data.result = {url: "ajax-sub2.json", debugDelay: 1000};
      },





    });
    $("#tree3").fancytree({
      extensions: ["dnd", "edit", "glyph", "wide", "childcounter", "filter"],
      checkbox: true,
      dnd: {
        focusOnClick: true,
        dragStart: function(node, data) { return true; },
        dragEnter: function(node, data) { return false; },
        dragDrop: function(node, data) { data.otherNode.copyTo(node, data.hitMode); }
      },
      glyph: glyph_opts,




      selectMode: 3,
      quicksearch: true,

      source: {{ countryDataReady|safe }},
      filter: {
        autoApply: true,  // Re-apply last filter if lazy data is loaded
        counter: true,  // Show a badge with number of matching child nodes near parent icons
        fuzzy: false,  // Match single characters in order, e.g. 'fb' will match 'FooBar'
        hideExpandedCounter: true,  // Hide counter badge, when parent is expanded
        highlight: true,  // Highlight matches by wrapping inside <mark> tags
        mode: "dimm"  // Grayout unmatched nodes (pass "hide" to remove unmatched node instead)
      },

      toggleEffect: { effect: "drop", options: {direction: "left"}, duration: 400 },
      wide: {
        iconWidth: "1em",     // Adjust this if @fancy-icon-width != "16px"
        iconSpacing: "0.5em", // Adjust this if @fancy-icon-spacing != "3px"
        levelOfs: "1.5em"     // Adjust this if ul padding != "16px"
      },

      icon: function(event, data){
        // if( data.node.isFolder() ) {
        //   return "glyphicon glyphicon-book";
        // }
      },
      childcounter: {
        deep: true,
        hideZeros: true,
        hideExpanded: true
      },

       activate: function(event, data) {
      },


      lazyLoad: function(event, data) {
        data.result = {url: "ajax-sub2.json", debugDelay: 1000};
      },





    });
    // Initialize Fancytree
    $("#tree").fancytree({
      extensions: ["dnd", "edit", "glyph", "wide", "childcounter", "filter"],
      checkbox: true,
      dnd: {
        focusOnClick: true,
        dragStart: function(node, data) { return true; },
        dragEnter: function(node, data) { return false; },
        dragDrop: function(node, data) { data.otherNode.copyTo(node, data.hitMode); }
      },
      glyph: glyph_opts,




      selectMode: 3,
      quicksearch: true,

      source: {{ sourceData|safe }},
      filter: {
        autoApply: true,  // Re-apply last filter if lazy data is loaded
        counter: true,  // Show a badge with number of matching child nodes near parent icons
        fuzzy: false,  // Match single characters in order, e.g. 'fb' will match 'FooBar'
        hideExpandedCounter: true,  // Hide counter badge, when parent is expanded
        highlight: true,  // Highlight matches by wrapping inside <mark> tags
        mode: "dimm"  // Grayout unmatched nodes (pass "hide" to remove unmatched node instead)
      },

      toggleEffect: { effect: "drop", options: {direction: "left"}, duration: 400 },
      wide: {
        iconWidth: "1em",     // Adjust this if @fancy-icon-width != "16px"
        iconSpacing: "0.5em", // Adjust this if @fancy-icon-spacing != "3px"
        levelOfs: "1.5em"     // Adjust this if ul padding != "16px"
      },

      icon: function(event, data){
        // if( data.node.isFolder() ) {
        //   return "glyphicon glyphicon-book";
        // }
      },
      childcounter: {
        deep: true,
        hideZeros: true,
        hideExpanded: true
      },

       activate: function(event, data) {
      },


      lazyLoad: function(event, data) {
        data.result = {url: "ajax-sub2.json", debugDelay: 1000};
      },





    });
    // Initialize Fancytree
    $("#tree4").fancytree({
      extensions: ["dnd", "edit", "glyph", "wide", "childcounter", "filter"],
      checkbox: true,
      dnd: {
        focusOnClick: true,
        dragStart: function(node, data) { return true; },
        dragEnter: function(node, data) { return false; },
        dragDrop: function(node, data) { data.otherNode.copyTo(node, data.hitMode); }
      },
      glyph: glyph_opts,




      selectMode: 3,
      quicksearch: true,

      source: {{ sourceData|safe }},
      filter: {
        autoApply: true,  // Re-apply last filter if lazy data is loaded
        counter: true,  // Show a badge with number of matching child nodes near parent icons
        fuzzy: false,  // Match single characters in order, e.g. 'fb' will match 'FooBar'
        hideExpandedCounter: true,  // Hide counter badge, when parent is expanded
        highlight: true,  // Highlight matches by wrapping inside <mark> tags
        mode: "dimm"  // Grayout unmatched nodes (pass "hide" to remove unmatched node instead)
      },

      toggleEffect: { effect: "drop", options: {direction: "left"}, duration: 400 },
      wide: {
        iconWidth: "1em",     // Adjust this if @fancy-icon-width != "16px"
        iconSpacing: "0.5em", // Adjust this if @fancy-icon-spacing != "3px"
        levelOfs: "1.5em"     // Adjust this if ul padding != "16px"
      },

      icon: function(event, data){
        // if( data.node.isFolder() ) {
        //   return "glyphicon glyphicon-book";
        // }
      },
      childcounter: {
        deep: true,
        hideZeros: true,
        hideExpanded: true
      },

       activate: function(event, data) {
      },


      lazyLoad: function(event, data) {
        data.result = {url: "ajax-sub2.json", debugDelay: 1000};
      },





    });


		$("form").submit(function() {
			// Render hidden <input> elements for active and selected nodes
			$("#tree2").fancytree("getTree").generateFormElements();
			$("#tree").fancytree("getTree").generateFormElements();
			$("#tree3").fancytree("getTree").generateFormElements();
			$("#tree4").fancytree("getTree").generateFormElements();




		});

$("#btnsToggleSelect").click(function(){
      $("#tree").fancytree("getRootNode").visit(function(node){
        node.toggleSelected();
      });
      return false;
    });
    $("#btnsDeselectAll").click(function(){
      $("#tree").fancytree("getTree").visit(function(node){
        node.setSelected(false);
      });
      return false;
    });
    $("#btnsSelectAll").click(function(){
      $("#tree").fancytree("getTree").visit(function(node){
        node.setSelected(true);
      });
      return false;
    });
    $("#btnsExpandAll").click(function(){
		$("#tree").fancytree("getTree").visit(function(node){
			node.setExpanded(true);
		});
	});
	$("#btnsCollapseAll").click(function(){
		$("#tree").fancytree("getTree").visit(function(node){
			node.setExpanded(false);
		});
	});

$("#btnsToggleSelect2").click(function(){
      $("#tree2").fancytree("getRootNode").visit(function(node){
        node.toggleSelected();
      });
      return false;
    });
    $("#btnsDeselectAll2").click(function(){
      $("#tree2").fancytree("getTree").visit(function(node){
        node.setSelected(false);
      });
      return false;
    });
    $("#btnsSelectAll2").click(function(){
      $("#tree2").fancytree("getTree").visit(function(node){
        node.setSelected(true);
      });
      return false;
    });
    $("#btnsExpandAll2").click(function(){
		$("#tree2").fancytree("getTree").visit(function(node){
			node.setExpanded(true);
		});
	});
	$("#btnsCollapseAll2").click(function(){
		$("#tree2").fancytree("getTree").visit(function(node){
			node.setExpanded(false);
		});
	});
	$("#btnsToggleSelect3").click(function(){
      $("#tree3").fancytree("getRootNode").visit(function(node){
        node.toggleSelected();
      });
      return false;
    });
    $("#btnsDeselectAll3").click(function(){
      $("#tree3").fancytree("getTree").visit(function(node){
        node.setSelected(false);
      });
      return false;
    });
    $("#btnsSelectAll3").click(function(){
      $("#tree3").fancytree("getTree").visit(function(node){
        node.setSelected(true);
      });
      return false;
    });
    $("#btnsExpandAll3").click(function(){
		$("#tree3").fancytree("getTree").visit(function(node){
			node.setExpanded(true);
		});
	});
	$("#btnsCollapseAll3").click(function(){
		$("#tree3").fancytree("getTree").visit(function(node){
			node.setExpanded(false);
		});
	});
	$("#btnsToggleSelect4").click(function(){
      $("#tree4").fancytree("getRootNode").visit(function(node){
        node.toggleSelected();
      });
      return false;
    });
    $("#btnsDeselectAll4").click(function(){
      $("#tree4").fancytree("getTree").visit(function(node){
        node.setSelected(false);
      });
      return false;
    });
    $("#btnsSelectAll4").click(function(){
      $("#tree4").fancytree("getTree").visit(function(node){
        node.setSelected(true);
      });
      return false;
    });
    $("#btnsExpandAll4").click(function(){
		$("#tree4").fancytree("getTree").visit(function(node){
			node.setExpanded(true);
		});
	});
	$("#btnsCollapseAll4").click(function(){
		$("#tree4").fancytree("getTree").visit(function(node){
			node.setExpanded(false);
		});
	});




var tree = $("#tree").fancytree("getTree");

$("input[name=search]").keyup(function(e){
      var n,
        opts = {
          autoExpand: $("#autoExpand").is(":checked"),
          leavesOnly: $("#leavesOnly").is(":checked")
        },
        match = $(this).val();





      if($("#regex").is(":checked")) {
        // Pass function to perform match
        n = tree.filterNodes(function(node) {
          return new RegExp(match, "i").test(node.title);
        }, opts);
      } else {
        // Pass a string to perform case insensitive matching
        n = tree.filterNodes(match, opts);
      }
      $("button#btnResetSearch").attr("disabled", true);
      $("span#matches").text("(" + n + " matches)");
    }).focus();

    $("button#btnResetSearch").click(function(e){
      $("input[name=search]").val("");
      $("span#matches").text("");
      tree.clearFilter();
    }).attr("disabled", true);

    $("fieldset input:checkbox").change(function(e){
      var id = $(this).attr("id"),
        flag = $(this).is(":checked");

      switch( id ) {
      case "autoExpand":
      case "regex":
      case "leavesOnly":
        // Re-apply filter only
        break;
      case "hideMode":
        tree.options.filter.mode = flag ? "hide" : "dimm";
        break;
      case "counter":
      case "fuzzy":
      case "hideExpandedCounter":
      case "highlight":
        tree.options.filter[id] = flag;
        break;
      }
      tree.clearFilter();
      $("input[name=search]").keyup();
    });

    $("#counter,#hideExpandedCounter,#highlight").prop("checked", true);

    addSampleButton({
      label: "Filter active branch",
      newline: false,
      code: function(){
        if( !tree.getActiveNode() ) {
          alert("Please activate a folder.");
          return;
        }
        tree.filterBranches(function(node){
          return node.isActive();
        });
      }
    });
    addSampleButton({
      label: "Reset filter",
      newline: false,
      code: function(){
        tree.clearFilter();
      }
    });
var tree4 = $("#tree4").fancytree("getTree");
$("input[name=search]").keyup(function(e){
      var n,
        opts = {
          autoExpand: $("#autoExpand").is(":checked"),
          leavesOnly: $("#leavesOnly").is(":checked")
        },
        match = $(this).val();





      if($("#regex").is(":checked")) {
        // Pass function to perform match
        n = tree4.filterNodes(function(node) {
          return new RegExp(match, "i").test(node.title);
        }, opts);
      } else {
        // Pass a string to perform case insensitive matching
        n = tree4.filterNodes(match, opts);
      }
      $("button#btnResetSearch").attr("disabled", true);
      $("span#matches").text("(" + n + " matches)");
    }).focus();

    $("button#btnResetSearch").click(function(e){
      $("input[name=search]").val("");
      $("span#matches").text("");
      tree4.clearFilter();
    }).attr("disabled", true);

    $("fieldset input:checkbox").change(function(e){
      var id = $(this).attr("id"),
        flag = $(this).is(":checked");

      switch( id ) {
      case "autoExpand":
      case "regex":
      case "leavesOnly":
        // Re-apply filter only
        break;
      case "hideMode":
        tree4.options.filter.mode = flag ? "hide" : "dimm";
        break;
      case "counter":
      case "fuzzy":
      case "hideExpandedCounter":
      case "highlight":
        tree4.options.filter[id] = flag;
        break;
      }
      tree4.clearFilter();
      $("input[name=search]").keyup();
    });

    $("#counter,#hideExpandedCounter,#highlight").prop("checked", true);

    addSampleButton({
      label: "Filter active branch",
      newline: false,
      code: function(){
        if( !tree4.getActiveNode() ) {
          alert("Please activate a folder.");
          return;
        }
        tree4.filterBranches(function(node){
          return node.isActive();
        });
      }
    });
    addSampleButton({
      label: "Reset filter",
      newline: false,
      code: function(){
        tree4.clearFilter();
      }
    });



  });