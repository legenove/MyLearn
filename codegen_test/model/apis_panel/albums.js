/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Albums = function () {
    /*
        @params obj 'data params'
            album_type   'string' album type in query
            creator_id   'integer' int id in query
            album_id   'string' album id in query
            title   'string' title in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            date_updated   'ref' 
            date_created   'ref' 
            image   'string' 
            id   'string' 
            icon   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/albums",
            method: "GET",
            data: {
                album_type: obj.album_type,
                creator_id: obj.creator_id,
                album_id: obj.album_id,
                title: obj.title,
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
    
    /*
        @params obj 'data params'
            album_type   'string' 
            description   'string' 
            title   'string' 
            order_score   'integer' 
            is_free   'boolean' 
            _image   'string' 
            creator_id   'integer' 
            share_description   'string' 
            is_show_showcase   'boolean' 
            is_show_title   'boolean' 
            _icon   'string' 
            
        @success
            status 200    type:object
            date_updated   'ref' 
            date_created   'ref' 
            image   'string' 
            id   'string' 
            icon   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/albums",
            method: "POST",
            data: {
                album_type: obj.album_type,
                description: obj.description,
                title: obj.title,
                order_score: obj.order_score,
                is_free: obj.is_free,
                _image: obj._image,
                creator_id: obj.creator_id,
                share_description: obj.share_description,
                is_show_showcase: obj.is_show_showcase,
                is_show_title: obj.is_show_title,
                _icon: obj._icon
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
    Albums: new Albums
};