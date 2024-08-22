create database tennis_stroke_process;

drop table if exists video
create table video
(
    video_id         bigint auto_increment comment 'Primary key of video'
        primary key,
    user_id          bigint        not null comment 'Foreign key with user',
    url              varchar(255)  null comment 'Video storgae url',
    is_live_streamed int default 0 not null comment 'Is live streamed or uploaded',
    length           bigint        not null comment 'Length of video in ms',
    created_date     datetime      not null comment 'Created date',
    created_by       varchar(255)  null comment 'Created by',
    updated_date     datetime      null comment 'Updated date',
    updated_by       varchar(255)  null comment 'Updated by',
    is_deleted       int default 0 not null comment 'Deleted'
);




drop table if exists swing
create table swing
(
    swing_id     bigint auto_increment comment 'Primary key of swing'
        primary key,
    video_id     bigint        not null comment 'Foriegn key of video',
    start_time   bigint        null comment 'Start time in ms from video',
    end_time     bigint        null comment 'End time in ms from video',
    swing_class  int           null comment 'Swing class: 1 for forehand, 2 for backhand, 3 for serve',
    avg_score    double        null comment 'Average score of this swing',
    created_date datetime      not null comment 'Created date',
    `created by` varchar(255)  null comment 'Created by',
    updated_date datetime      null comment 'Updated date',
    updated_by   varchar(255)  null comment 'Updated by',
    is_deleted   int default 0 not null comment 'Is deleted'
);


drop table if exists swing_key_frame
create table swing_key_frame
(
    swing_key_frame_id bigint auto_increment comment 'Primary key of swing key frame'
        primary key,
    swing_id           bigint           not null comment 'Foreign key of swing',
    nose_0_x           double default 0 not null comment 'Nose 0 X',
    nose_0_y           double default 0 not null comment 'Nose 0 Y',
    neck_1_x           double default 0 not null comment 'Neck 1 X',
    neck_1_y           double default 0 not null comment 'Neck 1 Y',
    r_shoulder_2_x     double           not null comment 'RShoulde 2 X',
    r_shoulder_2_y     double default 0 not null comment 'RShoulde 2 Y',
    r_elbow_3_x        double default 0 not null comment 'RElbow 3 X',
    r_elbow_3_y        double default 0 not null comment 'RElbow 3 Y',
    r_wrist_4_x        double default 0 not null comment 'RWrist 3 X',
    r_wrist_4_y        double default 0 not null comment 'RWrist 3 Y',
    l_shoulder_5_x     double           not null comment 'RShoulde 2 X',
    l_shoulder_5_y     double default 0 not null comment 'RShoulde 2 Y',
    l_elbow_6_x        double default 0 not null comment 'RElbow 3 X',
    l_elbow_6_y        double default 0 not null comment 'RElbow 3 Y',
    l_wrist_7_x        double default 0 not null comment 'RWrist 3 X',
    l_wrist_7_y        double default 0 not null comment 'RWrist 3 Y',
    r_hip_8_x          double           not null comment 'RShoulde 2 X',
    r_hip_8_y          double default 0 not null comment 'RShoulde 2 Y',
    r_knee_9_x         double default 0 not null comment 'RElbow 3 X',
    r_knee_9_y         double default 0 not null comment 'RElbow 3 Y',
    r_ankle_10_x       double default 0 not null comment 'RWrist 3 X',
    r_ankle_10_y       double default 0 not null comment 'RWrist 3 Y',
    l_hip_11_x         double           not null comment 'RShoulde 2 X',
    l_hip_11_y         double default 0 not null comment 'RShoulde 2 Y',
    l_knee_12_x        double default 0 not null comment 'RElbow 3 X',
    l_knee_12_y        double default 0 not null comment 'RElbow 3 Y',
    l_ankle_13_x       double default 0 not null comment 'RWrist 3 X',
    l_ankle_13_y       double default 0 not null comment 'RWrist 3 Y',
    r_eye_14_x         double           not null comment 'RShoulde 2 X',
    r_eye_14_y         double default 0 not null comment 'RShoulde 2 Y',
    l_eye_15_x         double default 0 not null comment 'RElbow 3 X',
    l_eye_15_y         double default 0 not null comment 'RElbow 3 Y',
    r_ear_16_x         double           not null comment 'RShoulde 2 X',
    r_ear_16_y         double default 0 not null comment 'RShoulde 2 Y',
    l_ear_17_x         double default 0 not null comment 'RElbow 3 X',
    l_ear_17_y         double default 0 not null comment 'RElbow 3 Y',
    stage              int              null comment 'Stage of swing',
    frame_time         bigint default 0 not null comment 'Time appears in the video',
    created_date       datetime         null comment 'Created date',
    created_by         varchar(255)     null comment 'Created by',
    updated_date       datetime         null comment 'Updated date',
    updated_by         varchar(255)     null comment 'Updated by'
);

