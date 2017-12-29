/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Questions = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            is_public   'boolean' is public in query
            is_recommended   'boolean' is recommended in query
            respondent_id   'integer' respondent id in query
            id   'string' string id in query
            status   'string' status in query
            review_status   'string' review status in query
            asker_nickname   'string' nickname in query
            respondent_nickname   'string' nickname in query
            respondent_is_verified   'boolean' is verified in query
            respondent_is_star   'boolean' is star in query
            respondent_verified_category   'string' verified category in query
            interval_from_succeed   'integer' interval in query
            answer_duration   'integer' duration in query
            order_by   'string' order by in query
            has_image   'boolean' has image in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            discussions_count   'integer' 
            date_updated   'ref' 
            is_recommended   'boolean' 
            order_score   'integer' 
            listenings_count   'integer' 
            images_count   'integer' 
            has_discussions   'boolean' 
            score   'integer' 
            topic_feed_id   'boolean' 
            is_hidden   'boolean' 
            _visitor_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions",
            method: "GET",
            data: {
                account_id: obj.account_id,
                is_public: obj.is_public,
                is_recommended: obj.is_recommended,
                respondent_id: obj.respondent_id,
                id: obj.id,
                status: obj.status,
                review_status: obj.review_status,
                asker_nickname: obj.asker_nickname,
                respondent_nickname: obj.respondent_nickname,
                respondent_is_verified: obj.respondent_is_verified,
                respondent_is_star: obj.respondent_is_star,
                respondent_verified_category: obj.respondent_verified_category,
                interval_from_succeed: obj.interval_from_succeed,
                answer_duration: obj.answer_duration,
                order_by: obj.order_by,
                has_image: obj.has_image,
                limit: obj.limit,
                offset: obj.offset,
                page: obj.page,
                per_page: obj.per_page
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    Questions: new Questions
};