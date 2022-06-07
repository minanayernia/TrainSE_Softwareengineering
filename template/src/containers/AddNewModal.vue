<template>
  <b-modal id="request" ref="request" :title="$t('Request')" size="md">
    <b-form>
      <b-form-group>
        <b-textarea
          v-model="request_text"
          :rows="7"
          :max-rows="20"
          placeholder="write your feature request here."
        />
      </b-form-group>
    </b-form>

    <template slot="modal-footer">
      <b-button variant="outline-secondary" @click="hideModal('request')">{{
        $t("pages.cancel")
      }}</b-button>
      <b-button variant="primary" @click="addNewItem()" class="mr-1">{{
        $t("pages.submit")
      }}</b-button>
    </template>
  </b-modal>
</template>
<script>
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
import { api } from "../constants/config";
import axios from "axios";
export default {
  components: {
    "v-select": vSelect
  },
  props: ["categories", "statuses", "id"],
  data() {
    return {
      request_text: ""
    };
  },
  methods: {
    addNewItem() {
      const data1 = {
        whoAsk: this.id,
        whoAnswer: null,
        request_text: this.request_text
      };
      console.log(data1);
      axios
        .post(api + "createquestion/", data1)
        .then(response => {
          console.log("req");
          console.log(response);
          return response.data;
        })
        .then(res => {
          this.hideModal("request");
          this.request_text = "";
        });
    },
    hideModal(refname) {
      this.$refs[refname].hide();
    }
  }
};
</script>
