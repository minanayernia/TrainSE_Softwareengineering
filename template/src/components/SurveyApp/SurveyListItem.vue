<template>
    <b-card no-body style="margin:5px;">

        <div class="d-flex flex-grow-1 min-width-zero">
            <b-card-body class="align-self-center d-flex flex-column flex-md-row justify-content-between min-width-zero align-items-md-center pb-2">
                <p v-if="currentUser.role=='A'" class="align-middle d-inline-block"><span class="font-weight-bold text-primary">{{data.whoAskName}} request:</span> "{{data.request_text}}".</p>
                <span v-if="data.notifType=='LC' && currentUser.role=='U'" class="align-middle d-inline-block">{{data.senderUsername}} liked your comment "{{data.commentText}}".  </span>
                <span v-if="data.notifType=='CR' && currentUser.role=='U'" class="align-middle d-inline-block">{{data.senderUsername}} replied your comment "{{data.commentText}}".  </span>
                <p v-if="currentUser.role=='U'"class="mb-1 text-muted text-small w-15 w-xs-100">{{convertFromStringToDate(data.date)}}</p>

            </b-card-body>

        </div>

        <div class="card-body pt-1"><p class="mb-0" v-html="data.detail"></p></div>

    </b-card>
</template>

<script>
import { adminRoot } from '../../constants/config'
import * as moment from 'jalali-moment';
import { mapGetters, mapMutations, mapActions } from "vuex";

export default {
  props: ['data', 'selectedItems'],
  data(){
    return{
      adminRoot
    }
  },
  methods: {
    convertFromStringToDate(responseDate) {
      let dateComponents = responseDate.split('T');
      let datePieces = dateComponents[0].split("-");
      let timePieces = dateComponents[1].split(":");
      let date=new Date(datePieces[2], (datePieces[1] - 1), datePieces[0],timePieces[0], timePieces[1], timePieces[2])
      return(moment(datePieces[0]+'-'+datePieces[1]+'-'+datePieces[2]+' '+timePieces[0]+':'+timePieces[1]+':'+timePieces[2], 'YYYY-M-D HH:mm:ss')
      .locale('fa')
      .format('YYYY/M/D - HH:mm:ss').toString())
    },
    toggleItem (event, itemId) {
      
      this.$emit('toggle-item', event, itemId)
    }
  },
  computed: {
    ...mapGetters({
      currentUser: "currentUser",

    })
  },
}
</script>
