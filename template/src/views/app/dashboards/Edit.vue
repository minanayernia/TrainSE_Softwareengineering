
<template>
  <b-modal
    id="modall"
    ref="modall"
    title="Edit Category"
    size="md"
    hide-footer
  >
    <b-card no-body>
      <b-card-body class="wizard wizard-default">
              <b-form>
                <b-form-group label="Title:">
                  <b-form-input v-model="title" placeholder="enter title of category"/>
                </b-form-group>
                
              <button
                type="button"
                class="btn btn-primary"
                @click="addNewItem"
              >
                submit
              </button>
              </b-form>
      </b-card-body>
    </b-card>
  </b-modal>
</template>

<script>
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import Tab from "../../../components/Form/Wizard/Tab";

import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";

import VueDropzone from "vue2-dropzone";
import { mapGetters, mapMutations, mapActions } from "vuex";

import { quillEditor } from "vue-quill-editor";
import { apiUrl ,api } from "../../../constants/config";
import axios from "axios";
import FormWizard from "../../../components/Form/Wizard/FormWizard";

export default {
  components: {
    "v-select": vSelect,
    Tab,
    FormWizard,
    "vue-dropzone": VueDropzone,
  },
  props: ["categoryID","ItemID"],
  data() {
    return {
      title:"",
      error: "",

      mainImageDropzoneOptions: {
        url: `${apiUrl}/upload`,
        thumbnailHeight: 150,
        maxFilesize: 2,
        maxFiles: 1,
        acceptedFiles: "image/*",
        dictDefaultMessage: "drop image of tutorial in this box",
        previewTemplate: this.dropzoneTemplate(),
      }

    };
  },
  computed: {
    ...mapGetters({
      currentUser: "currentUser",
      menuType: "getMenuType",
      menuClickCount: "getMenuClickCount",
      selectedMenuHasSubItems: "getSelectedMenuHasSubItems"
    }),

  },
  methods: {
    getCategory(){
      const data1={
        category_id:this.ItemID,
      }
      axios
        .post(api+"getCategoryByID/",data1)
        .then(response => {
          console.log("resource list");
          console.log(response);
          return response.data;
        })
        .then(res => {
            this.title=res.name;
        }); 
    },

    addNewItem() {
      const resource = {
        category_id: this.ItemID,
        creator_id:this.currentUser.id,
        title: this.title,
      };
      axios
        .post(`${api}updateCategory/`, resource)
        .then((response) => {
          return response.data;
        })
        .then((res) => {
          console.log("add new category")
          console.log(res);
          this.hideModal("modall");
          this.title = "";
          this.$emit('update');
        });
    },

    hideModal(refname) {
      this.$refs[refname].hide();
    },

    dropzoneTemplate() {
      return `<div class="dz-preview dz-file-preview mb-3">
                <div class="d-flex flex-row "> 
                  <div class="p-0 w-30 position-relative">
                    <div class="dz-error-mark"><span><i></i>  </span></div>
                    <div class="dz-success-mark"><span><i></i></span></div>
                    <div class="preview-container">
                      <img data-dz-thumbnail class="img-thumbnail border-0" />
                      <i class="simple-icon-doc preview-icon"></i>
                    </div>
                  </div>
                  <div class="pl-3 pt-2 pr-2 pb-1 w-40 dz-details position-relative m-2">
                    <div> <span data-dz-name style="direction:ltr" /> </div>
                    <div class="text-primary text-extra-small" style="direction:ltr" data-dz-size /> </div>
                    <div class="dz-progress"><span class="dz-upload" data-dz-uploadprogress></span></div>
                    <div class="dz-error-message"><span data-dz-errormessage></span></div>
                  </div>
                  <a href="#" class="remove" data-dz-remove> <i class="glyph-icon simple-icon-trash"></i> </a>
                </div>
              </div>
        `;
    },

    mainImageUploadSuccess(file, response) {
      this.newItem.mainImage = response.url;
    },
    mainImageDeleteFile(file, error, xhr) {
      console.log(file);
      console.log(error);
      console.log(xhr);
    },
  },
  mounted() {
    this.getCategory();
  },
  watch:{
    ItemID: function (val, oldVal) {
      this.getCategory();
    },
  }
};
</script>

