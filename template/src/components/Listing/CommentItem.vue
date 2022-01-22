<template>

<div class="d-flex flex-row mb-3 pb-3 border-bottom" style="position: relative;">
    
    <router-link tag="a" :to="detailPath">
        <img src="/assets/img/profiles/l-1.jpg" class="img-thumbnail border-0 rounded-circle list-thumbnail align-self-center xsmall" />
    </router-link>

    <div class="pl-3 pr-2">
        <router-link tag="a" :to="detailPath">
            <p class="font-weight-medium mb-0 " maxlength = "10">{{ data.text }}</p>
            <p class="text-muted mb-1 text-small">{{ convertFromStringToDate(data.create_date) }}</p>
            <div>
                <i class="iconsminds-like">{{data.likecommentcount}}</i>
            </div>
        </router-link>
    </div>
    <div class="navbar-right">
        <button @click="replyComment(data.comment_id)" style="position: absolute;right: 0px;top: 5px;" class="btn btn-primary" >report</button>
        <button @click="likeComment(data.comment_id)" style="position: absolute;right: 80px;top: 5px;" class="btn btn-primary" >like</button>
    </div>
</div>
    
</template>

<script>
import Stars from '../Common/Stars'
import * as moment from 'jalali-moment';

export default {
    components: {
        'stars': Stars
    },
    methods:{
        convertFromStringToDate(responseDate) {
            let dateComponents = responseDate.split('T');
            let datePieces = dateComponents[0].split("-");
            let timePieces = dateComponents[1].split(":");
            let date=new Date(datePieces[2], (datePieces[1] - 1), datePieces[0],timePieces[0], timePieces[1], timePieces[2])
            return(moment(datePieces[0]+'-'+datePieces[1]+'-'+datePieces[2], 'YYYY-M-D HH:mm:ss')
            .locale('en')
            .format('YYYY/M/D').toString())
        }
    },
    props: ['data', 'detailPath','replyComment',"likeComment"]
}
</script>
